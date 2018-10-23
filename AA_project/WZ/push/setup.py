from cx_Freeze import setup, Executable
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(CURRENT_DIR, "config.ini")
CONFIG_FILE = os.path.abspath(CONFIG_FILE)

include_files = [CONFIG_FILE]


build_exe_options = {"packages": ["os"],
                     "include_files": include_files}

setup(
    name='monitor',
    version='1.0',
    description='',
    author='',
    author_email='',
    options={'build_exe': build_exe_options},
    executables=[Executable('monitor.py')]
)