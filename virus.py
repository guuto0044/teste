from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == 'win32':
    base = None
executables = [Executable('ransomware.py',base=base)]
packages = ['idna']
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name = 'Ransomware',
    options = options,
    version = '1.0',
    description = 'The malware active',
    executables = executables
)