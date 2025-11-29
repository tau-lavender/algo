import typer # type: ignore

import src.benchmark.benchmark


app = typer.Typer()


@app.command() # поддержка отрицательных чисел
def benchmark_sorts() -> None:
    src.benchmark.benchmark.benchmark_sorts()
