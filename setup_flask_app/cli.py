import typer
import os
from typing_extensions import Annotated

app = typer.Typer()

directories = ['static', 'templates']
files = ['__init__.py']

@app.command()
def create_app(name: str = typer.Argument(), boostrap: Annotated[bool, typer.Option(help="This is to setup boostrap along with app")] = False):
    try:

        if boostrap:
            print("working")
        
        if not os.path.exists(name):
            os.makedirs(name)

    except Exception as e:
        typer.echo(f"Error setting up app :  {e}")
        typer.Exit(code=1)


if __name__ == "__main__":
    app()
