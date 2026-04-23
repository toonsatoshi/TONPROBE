# Address investigation report

Date: 2026-04-23 (UTC)

## Scope

- Investigated 17 TON user-friendly addresses provided by the user.
- Per-address checks: base64url decode, CRC16-XMODEM checksum, tag flags, workchain, and raw hex form.
- Attempted live on-chain lookup through toncenter public API, but outbound HTTP requests were blocked in this execution environment (403 tunnel failure).

## Results

| # | Address | Valid | Bounceable | Testnet-only | Workchain | Raw address | Network lookup |
|---:|---|---|---|---|---:|---|---|
| 1 | `EQABJbeBvBOieb62gZTHKFUfWaV21KvqMbqEnYNaQRrxlEQJ` | True | True | False | 0 | `0:0125b781bc13a279beb68194c728551f59a576d4abea31ba849d835a411af194` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 2 | `EQAC0FL1JsOazRYwDC-Z7YKMQRBEVT1b5Y4JmDjKivMsdwdo` | True | True | False | 0 | `0:02d052f526c39acd16300c2f99ed828c411044553d5be58e099838ca8af32c77` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 3 | `EQAH1FMYeorW9pfNj06Qe94X8pikkv-x-8b_syVWoB8qGIEt` | True | True | False | 0 | `0:07d453187a8ad6f697cd8f4e907bde17f298a492ffb1fbc6ffb32556a01f2a18` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 4 | `EQAVq7aFD3SsRccxflRk_QX4PJi1wEbVoQAAUg49tZC_M7vf` | True | True | False | 0 | `0:15abb6850f74ac45c7317e5464fd05f83c98b5c046d5a10000520e3db590bf33` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 5 | `EQAlV7VyQzXNIXZVyiCPoJznoi_5ir7_scHO9QAQmSXMXn6y` | True | True | False | 0 | `0:2557b5724335cd217655ca208fa09ce7a22ff98abeffb1c1cef500109925cc5e` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 6 | `EQB-jk2bfRJwFK_BEGdAywPYBGCrfMdUgMTOQ3ogqaF0697V` | True | True | False | 0 | `0:7e8e4d9b7d127014afc1106740cb03d80460ab7cc75480c4ce437a20a9a174eb` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 7 | `EQBMVk8uLQZJvIsSn5G5K3etrkFQVjd6F_LqcM5_EOQHr48b` | True | True | False | 0 | `0:4c564f2e2d0649bc8b129f91b92b77adae415056377a17f2ea70ce7f10e407af` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 8 | `EQBoyhKi9OSSnXaw-jT8TXbQ6knCMqxW69E2bauyp8-6fEB9` | True | True | False | 0 | `0:68ca12a2f4e4929d76b0fa34fc4d76d0ea49c232ac56ebd1366dabb2a7cfba7c` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 9 | `EQBrtZnDdd7wd1n4kFPoJRS7fPurVw-2E6FeJ2WXY8QVMnN4` | True | True | False | 0 | `0:6bb599c375def07759f89053e82514bb7cfbab570fb613a15e27659763c41532` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 10 | `EQCFo-ukD_OWdyB2rZLQZkh55oT1WFaxdrmitgDhQd5DuSoW` | True | True | False | 0 | `0:85a3eba40ff396772076ad92d0664879e684f55856b176b9a2b600e141de43b9` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 11 | `EQCZSs8f0Z4fhe8b7emzW3_HnMv3ofjC_zOXVx0WSlGT5WqI` | True | True | False | 0 | `0:994acf1fd19e1f85ef1bede9b35b7fc79ccbf7a1f8c2ff3397571d164a5193e5` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 12 | `EQCfErFthrD4fJEUvqZqBQAEAQ9TDas-KSCfhEzEAsBMnYBb` | True | True | False | 0 | `0:9f12b16d86b0f87c9114bea66a050004010f530dab3e29209f844cc402c04c9d` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 13 | `EQCxUPY6FqKtNs4204EdZ9K6lolp8WJs65k8_Jg9xVGaKfDY` | True | True | False | 0 | `0:b150f63a16a2ad36ce36d3811d67d2ba968969f1626ceb993cfc983dc5519a29` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 14 | `EQD5uKKrQQWiLEnFZlEdNRxsLPf3NVdcZrYt-3ghNG3EIL1t` | True | True | False | 0 | `0:f9b8a2ab4105a22c49c566511d351c6c2cf7f735575c66b62dfb7821346dc420` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 15 | `EQDMZIw6ZGbZEsR509GDsPGsQhR5M4Z0FyU4Rc53pxRgbRAZ` | True | True | False | 0 | `0:cc648c3a6466d912c479d3d183b0f1ac42147933867417253845ce77a714606d` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 16 | `EQDr88p8B3ru_qMwQkdWSs0C7UVBuBwLGP4koDVyGmzj3VVe` | True | True | False | 0 | `0:ebf3ca7c077aeefea3304247564acd02ed4541b81c0b18fe24a035721a6ce3dd` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |
| 17 | `EQDspq9tRyKRy4VLt1RTNrVKUxbN79w6oEbc2jv7przy-Cmo` | True | True | False | 0 | `0:eca6af6d472291cb854bb7545336b54a5316cdefdc3aa046dcda3bfba6bcf2f8` | `network lookup failed: <urlopen error Tunnel connection failed: 403 Forbidden>` |

## Findings summary

- All 17 addresses are structurally valid TON user-friendly addresses (checksum verified).
- All addresses have tag `0x11`, meaning **bounceable** mainnet format (not testnet-only).
- All addresses are in workchain `0`.
- Due to network restrictions in this runtime, no balance/activity/contract state data could be fetched from public TON APIs.
