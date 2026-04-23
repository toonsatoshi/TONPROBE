"""CLI entrypoint for TONPROBE."""

import typer

app = typer.Typer(help="TONPROBE pipeline CLI")


@app.command()
def run() -> None:
    """Run the full pipeline."""
    typer.echo("TONPROBE run placeholder")


@app.command()
def ingest() -> None:
    typer.echo("Ingestion placeholder")


@app.command()
def analyze() -> None:
    typer.echo("Static/semantic analysis placeholder")


@app.command()
def fuzz() -> None:
    typer.echo("Dynamic fuzzing placeholder")


@app.command()
def review() -> None:
    typer.echo("Review queue placeholder")


@app.command()
def export() -> None:
    typer.echo("Export placeholder")


if __name__ == "__main__":
    app()
