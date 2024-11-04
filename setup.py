import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.


opts = {'includes' : ['re',"tkinter"], 'packages': ['pyttsx3.drivers',"os",
'pyttsx3.drivers.sapi5']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MAX",
        version = "1.1",
        description = "This is MAX made by HARSH JOSHI",
        options = {"build_exe": opts},
        author = "HARSH JOSHI",
        executables = [Executable("MAX.py", icon="icon.ico", base=base)])