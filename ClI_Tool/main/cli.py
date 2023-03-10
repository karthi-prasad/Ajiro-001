# import necessary stuffs
import typer
from typing import Optional
from ClI_Tool.main.main import __app_name__, __version__


app = typer.Typer()

def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        "--add computer",
        "--add repeater",
        "--set_device_strength",
        "--connect",
        "--info_route",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
):
    return

