#!/usr/bin/env python3

# install distutils
# Ubuntu/Debian: sudo apt install python3-distutils
# Build module: python3 setup.py build
# Install module: python3 setup.py install 
#   install venv env without conflict

from distutils.core import setup, Extension

def main():
    setup(name="fputs",
          version="0.0.1",
          description="Python interface to fputs C library function",
          author="Gall Anonymous",
          author_email="gall@anonymous.com",
          ext_modules=[Extension("fputs", ["fputs_module2.c"])])

if __name__ == "__main__":
    main()
