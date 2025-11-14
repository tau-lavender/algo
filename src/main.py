# import os
import importlib
import inspect

import typer # type: ignore

from src.configs.func_import_config import FUNC_IMPORT_CONFIG
# from src.constants import PATH_TO_CURRENT_PATH


app = typer.Typer()


if __name__ == "__main__":
    # # загружает файл где xранится cwd, создаёт если не существует
    # try:
    #     with open(PATH_TO_CURRENT_PATH) as f:
    #         current_path = f.readline().rstrip()
    # except FileNotFoundError:
    #     with open(PATH_TO_CURRENT_PATH, "w") as f:
    #         current_path = os.getcwd()
    #         f.write(current_path)
    # os.chdir(path=current_path)

    # импортирует команды обьявленные в конфиге
    for func_name in FUNC_IMPORT_CONFIG:
        try:
            mod = importlib.import_module(func_name)
            functions = inspect.getmembers(mod, inspect.isfunction)
            for foo in functions:
                if foo[0] == func_name[func_name.rfind(".") + 1:]:
                    app.command()(foo[1])
                    break
            else:
                raise ImportError
        except ImportError:
            print(f"{func_name} not imported")

    # запускает приложение typer
    try:
        app()
    except OSError as e:
        print(f"OSError: {e}")
