import typer
import os
import shutil

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