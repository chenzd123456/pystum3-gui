import PyInstaller.__main__
import os
import click
import shutil

EXEC_NAME = 'pystum3-gui'
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'assets', 'config.json')
ENTRY_FILE = os.path.join(os.path.dirname(__file__), 'src', 'main.py')
DIST_PATH = os.path.join(os.path.dirname(__file__), 'dist')

@click.group()
def cli():
    pass

@cli.command()
def build():
    PyInstaller.__main__.run([
        '--onefile',
        '--window',
        f'--name={EXEC_NAME}',
        f'--distpath={DIST_PATH}',
        f'{ENTRY_FILE}',
    ])

    shutil.copyfile(CONFIG_PATH, os.path.join(DIST_PATH, 'config.json'))

@cli.command()
def clean():
    print("clean...")
    delete_path("./build")
    delete_path("./dist")

if __name__ == "__main__":
    cli()