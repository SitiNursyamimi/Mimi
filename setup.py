import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base ="Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\User\AppData\Local\Programs\Python\Python311\tcl\tcl6.8"
os.environ['TK_LIBRARY'] = r"C:\Users\User\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("FRASys_Software.py", base=base, icon="face.ico")]

cx_Freeze.setup
(
    name = "FRASys Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll','image','data','Attendance Data Excel']}}
    version = "1.0",
    description = "Face Recognition Attendance System | Syamimi",
    executables =  executables
)   