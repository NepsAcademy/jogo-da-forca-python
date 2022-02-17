import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="resources/icon.ico",
)

build_exe_options = dict(
    include_files=["resources/"]
)  # folder,relative path. Use tuple like in the single file to set a absolute path.

setup(
    name="Jogo da Forca",
    version="0.1",
    description="Jogo da Forca",
    options={"build_exe": build_exe_options},
    executables=[target],
)
