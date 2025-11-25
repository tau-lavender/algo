# import os
import importlib
import inspect

import typer # type: ignore

from src.configs.func_import_config import FUNC_IMPORT_CONFIG


app = typer.Typer()


def import_func(func_name: str) -> None:
    """
    Импортирует функцию по имени её файла
    Имя файла должно соответствовать имени функции
    """
    mod = importlib.import_module(func_name)
    functions = inspect.getmembers(mod, inspect.isfunction)
    for foo in functions:
        if foo[0] == func_name[func_name.rfind(".") + 1:]:
            app.command(context_settings={"ignore_unknown_options": True})(foo[1])
            return None
    raise ImportError


def main() -> None:
    """
    Импортирует модули и запускает приложение
    :return: Ничего
    """

    # импортирует модули обьявленные в конфиге
    for func_name in FUNC_IMPORT_CONFIG:
        try:
            import_func(func_name)
        except ImportError:
            print(f"{func_name} not imported")

    # запускает приложение typer
    try:
        app()
    except OSError as e:
        print(f"OSError: {e}")


if __name__ == "__main__":
    main()
