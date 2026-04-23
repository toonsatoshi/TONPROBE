"""CLI entrypoint for TONPROBE."""

import json
from dataclasses import asdict
from pathlib import Path
from typing import Annotated, Literal

import typer

from tonprobe.findings.manager import FindingsManager

app = typer.Typer(help="TONPROBE pipeline CLI")

OutputFormat = Literal["json", "jsonl"]


def _serialize_findings(findings: list, fmt: OutputFormat, *, pretty: bool) -> str:
    records = [asdict(finding) for finding in findings]
    if fmt == "jsonl":
        return "\n".join(json.dumps(record) for record in records)
    if pretty:
        return json.dumps(records, indent=2)
    return json.dumps(records)


@app.command()
def run(
    targets: Annotated[
        list[str] | None,
        typer.Argument(help="Source files to analyze"),
    ] = None,
    fmt: Annotated[
        OutputFormat,
        typer.Option("--format", "-f", help="Output format."),
    ] = "json",
    output: Annotated[
        Path | None,
        typer.Option(
            "--output",
            "-o",
            help="Write output to a file path instead of stdout.",
        ),
    ] = None,
    pretty: Annotated[
        bool,
        typer.Option("--pretty/--compact", help="Use indented JSON output."),
    ] = True,
) -> None:
    """Run the full pipeline."""
    resolved_targets = targets or ["contracts/wallet.fc", "api/ton.py"]
    findings = FindingsManager().run(resolved_targets)
    rendered = _serialize_findings(findings, fmt, pretty=pretty)
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        typer.echo(f"Wrote findings to {output}")
        return
    typer.echo(rendered)


@app.command()
def ingest() -> None:
    typer.echo("Use `tonprobe run` to execute ingestion + analysis pipeline.")


@app.command()
def analyze() -> None:
    typer.echo("Use `tonprobe run` to execute static + semantic analysis.")


@app.command()
def fuzz() -> None:
    typer.echo("Use `tonprobe run` to execute dynamic validation.")


@app.command()
def review() -> None:
    typer.echo("Use `tonprobe run` and consume sorted findings output.")


@app.command()
def export() -> None:
    typer.echo("JSON export is emitted directly by `tonprobe run`.")


if __name__ == "__main__":
    app()
