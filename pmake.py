import PyInstaller.__main__
import os
import click
import shutil
import logging

EXEC_NAME = 'pystun3-gui'
DATA_PATH = os.path.join('data')
ENTRY_FILE = os.path.join('src', 'main.py')
DIST_PATH = os.path.join('dist')
BUILD_CACHE_PATH = os.path.join('build')
SPEC_PATH = os.path.join('spec')

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('pmake.log')
        ]
    )

@click.group()
def cli():
    setup_logging()
    logging.info("CLI initialized")

@cli.command()
def build():
    logging.info("Starting build process")
    PyInstaller.__main__.run([
        '--onefile',
        '--window',
        f'--name={EXEC_NAME}',
        f'--distpath={DIST_PATH}',
        f'--workpath={BUILD_CACHE_PATH}',
        f'--specpath={SPEC_PATH}',
        f'{ENTRY_FILE}',
    ])
    logging.info("Build process completed")
    # Copy data files to dist directory
    logging.info("Copying data files to dist directory")
    if os.path.exists(os.path.join(DIST_PATH, DATA_PATH)):
        shutil.rmtree(os.path.join(DIST_PATH, DATA_PATH))
    shutil.copytree(DATA_PATH, os.path.join(DIST_PATH, DATA_PATH))

@cli.command()
def clean():
    logging.info("Starting clean process")
    shutil.rmtree(BUILD_CACHE_PATH)
    shutil.rmtree(DIST_PATH)
    shutil.rmtree(SPEC_PATH)

if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}", exc_info=True)
        raise