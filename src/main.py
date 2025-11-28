from typer_shell import make_typer_shell # type: ignore

from src.functions.app import app as functions_app
from src.gen_test_case.app import app as gen_app
from src.sorts.app import app as sorts_app


app = make_typer_shell(prompt = "$: ",
                       intro="Алгоритмический мини-пакет. 'help' для информации о командах")


def main() -> None:
    """
    Импортирует модули и запускает приложение
    :return: Ничего
    """

    app.add_typer(functions_app)
    app.add_typer(sorts_app)
    app.add_typer(gen_app)

    app()


if __name__ == "__main__":
    main()
