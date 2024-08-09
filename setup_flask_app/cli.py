import typer
import os
from typing_extensions import Annotated
import shutil
from .funcs import create_directories, create_files, copy_template_files, write_content_into_files

app = typer.Typer()

directories = ['static', 'templates']
files = ['__init__.py']

def create_directories(parent_directory: str ,directories_list: list):
    print("making directories")
    with typer.progressbar(directories_list) as progress:
        for dir in progress:
            if not os.path.exists(f"./{parent_directory}/{dir}"):
                os.mkdir(f"./{parent_directory}/{dir}")
                progress.update(1)

def create_files(parent_directory: str ,files_list: list):
    print("making files")
    with typer.progressbar(files_list) as progress:
        for file in progress:
            if not os.path.exists(f"./{parent_directory}/{file}"):
                open(f"./{parent_directory}/{file}", 'w').close()
                progress.update(1)

def write_content_into_files(parent_directory: str, files_list: list):
    for file in files_list:
        with open(f"{parent_directory}/{file}", 'w') as f:
            print(f.name)
            f.write('''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
''')
            
def copy_template_files(parent_directory: str):
    dirs = os.listdir('./templates')
    for dir in dirs:
        if dir == 'static':
            files = os.listdir('./templates/static')
            for file in files:
                shutil.copy(f"./templates/static/{file}", f"{parent_directory}/static")
                continue

        if dir == 'templates':
            files = os.listdir('./templates/templates')
            for file in files:
                shutil.copy(f"./templates/templates/{file}", f"{parent_directory}/templates")
                continue
            
def delete_app(app_name):
    if os.path.exists(app_name):
        shutil.rmtree(app_name)

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
