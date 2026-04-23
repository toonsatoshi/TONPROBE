#!/usr/bin/env python3
"""Inspect TON user-friendly addresses.

The script validates address encoding and prints core metadata:
- checksum validity
- bounceability/testnet flags
- workchain id
- raw address (wc:hex)

Optionally, it can attempt an on-chain lookup through toncenter's public API.
"""

from __future__ import annotations

import argparse
import base64
import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass


@dataclass
class AddressInfo:
    address: str
    valid: bool
    reason: str
    tag: int | None = None
    is_bounceable: bool | None = None
    is_testnet_only: bool | None = None
    workchain: int | None = None
    account_hex: str | None = None

    @property
    def raw(self) -> str | None:
        if self.workchain is None or self.account_hex is None:
            return None
        return f"{self.workchain}:{self.account_hex}"


def crc16_xmodem(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc


def parse_ton_address(address: str) -> AddressInfo:
    addr = address.strip()
    if not addr:
        return AddressInfo(address=address, valid=False, reason="empty")

    if ":" in addr:
        wc, _, account = addr.partition(":")
        is_hex = len(account) == 64 and all(c in "0123456789abcdefABCDEF" for c in account)
        if wc.lstrip("-").isdigit() and is_hex:
            return AddressInfo(
                address=address,
                valid=True,
                reason="valid raw address",
                workchain=int(wc),
                account_hex=account.lower(),
            )
        return AddressInfo(address=address, valid=False, reason="invalid raw format")

    try:
        payload = base64.urlsafe_b64decode(addr + "=" * (-len(addr) % 4))
    except Exception:
        return AddressInfo(address=address, valid=False, reason="invalid base64url")

    if len(payload) != 36:
        return AddressInfo(address=address, valid=False, reason=f"unexpected payload length {len(payload)}")

    body, checksum = payload[:-2], int.from_bytes(payload[-2:], "big")
    if crc16_xmodem(body) != checksum:
        return AddressInfo(address=address, valid=False, reason="checksum mismatch")

    tag = body[0]
    wc = body[1] if body[1] < 128 else body[1] - 256
    account_hex = body[2:34].hex()

    # Reference tags are 0x11 (bounceable) and 0x51 (non-bounceable), with
    # optional testnet bit 0x80 set.
    base_tag = tag & 0x7F
    if base_tag not in (0x11, 0x51):
        reason = f"valid checksum but uncommon tag 0x{tag:02x}"
    else:
        reason = "valid user-friendly address"

    return AddressInfo(
        address=address,
        valid=True,
        reason=reason,
        tag=tag,
        is_bounceable=base_tag == 0x11,
        is_testnet_only=bool(tag & 0x80),
        workchain=wc,
        account_hex=account_hex,
    )


def query_toncenter(address: str, timeout: float = 10.0) -> dict:
    params = urllib.parse.urlencode({"address": address})
    url = f"https://toncenter.com/api/v2/getAddressInformation?{params}"
    request = urllib.request.Request(url=url, headers={"User-Agent": "tonprobe-address-inspector/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect TON addresses")
    parser.add_argument("addresses", nargs="+", help="TON address values to inspect")
    parser.add_argument(
        "--with-network",
        action="store_true",
        help="Attempt live lookup via toncenter public endpoint",
    )
    args = parser.parse_args()

    rows = []
    for addr in args.addresses:
        info = parse_ton_address(addr)
        row = {
            "address": info.address,
            "valid": info.valid,
            "reason": info.reason,
            "tag": f"0x{info.tag:02x}" if info.tag is not None else None,
            "bounceable": info.is_bounceable,
            "testnet_only": info.is_testnet_only,
            "workchain": info.workchain,
            "raw": info.raw,
            "network": None,
        }
        if args.with_network:
            try:
                row["network"] = query_toncenter(info.address)
            except urllib.error.URLError as err:
                row["network"] = {"error": f"network lookup failed: {err}"}
            except Exception as err:  # pragma: no cover - safety net
                row["network"] = {"error": f"unexpected error: {err}"}
        rows.append(row)

    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
