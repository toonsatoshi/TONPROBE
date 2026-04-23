"""CLI entrypoint for TONPROBE."""

import json
from typing import Annotated

import typer

from tonprobe.findings.manager import FindingsManager

app = typer.Typer(help="TONPROBE pipeline CLI")


@app.command()
def run(
    targets: Annotated[
        list[str] | None,
        typer.Argument(help="Source files to analyze"),
    ] = None,
) -> None:
    """Run the full pipeline."""
    resolved_targets = targets or ["contracts/wallet.fc", "api/ton.py"]
    findings = FindingsManager().run(resolved_targets)
    typer.echo(json.dumps([finding.__dict__ for finding in findings], indent=2))


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
