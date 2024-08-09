import typer
import os
from typing_extensions import Annotated
import shutil
from .funcs import create_directories, create_files, copy_template_files, write_content_into_files

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
        

        create_directories(name, directories)

        create_files(name, files)

        write_content_into_files(name, files)

        copy_template_files(f"{name}")

    except Exception as e:
        typer.echo(f"Error setting up app :  {e}")
        typer.Exit(code=1)


if __name__ == "__main__":
    app()
