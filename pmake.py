import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    os.path.join(os.path.dirname(__file__), 'src', 'main.py'),
    '--onefile',
    '--name=pystum3-gui',
    '--clean',
    '--window',
    '--noupx',
])