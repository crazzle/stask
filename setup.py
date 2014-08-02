__author__ = 'mark'

from py2exe.build_exe import py2exe
from distutils.core import setup

setup(
     name = "stask",
     version = "1.0",
     author = "Mark Keinhoerster",
     author_email = "",
     py_modules = ["Application","pyHook","pywin32"],
     packages = ["api", "helper","interactions","libs"],
     windows=["Application.py"],
     )


# invocation commands:
#
# Build exe file
# python setup.py py2exe
#
# Build distribution
# python setup.py bdist_wininst
