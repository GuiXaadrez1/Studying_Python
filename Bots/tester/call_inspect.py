from subprocess import Popen


PATH_INSPECT:str = r"C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64\inspect.exe"

Popen(PATH_INSPECT,shell=True)