import sys
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icons/icon.ico', 'icons/', 'menu_bar.py', 'main.qss', 'menu_bar.qss', 'screens/', 'menu_icons/']

build_exe_options = {"packages": ["os"], 'include_files': files}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="icons/icon.ico"
)

setup(
    name="Test",
    version="1.0",
    description="Test",
    author="Test",
    options={'build_exe': build_exe_options},
    executables=[target]
)
