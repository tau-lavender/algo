import typer # type: ignore

from src.functions.app import app as functions_app
from src.gen_test_case.app import app as gen_app
from src.sorts.app import app as sorts_app


app = typer.Typer()


def main() -> None:
    """
    Импортирует модули и запускает приложение
    :return: Ничего
    """

    app.add_typer(functions_app)
    app.add_typer(gen_app)
    app.add_typer(sorts_app)

    app()


if __name__ == "__main__":
    main()
