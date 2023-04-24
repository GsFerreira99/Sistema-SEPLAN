from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    "packages": ["os","sys","ctypes", "sqlalchemy", "MySQLdb"],
    'include_files': ['icon.ico', 'base.pdf', 'Calibri.ttf', 'credenciais.json'],
    "excludes": ["tkinter", ],
    'include_msvcr': True}



# base="Win32GUI" should be used only for Windows GUI app

setup(
    name = "Sistema SEPLAN",
    version = "1.1.1",
    description = "Interface",
    options = {"build_exe": build_exe_options},
    data_files = [ ('', ['icon.ico']), ('', ['credenciais.json']), ('', ['base.pdf']), ('', ['Calibri.ttf'])],
    executables = [Executable(
    script="main.py",
    icon="icon.ico",
    base = "Win32GUI"
    )]
)