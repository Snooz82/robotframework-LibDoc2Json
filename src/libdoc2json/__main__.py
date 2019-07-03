import sys
import os
from robot.libdoc import libdoc
from .libdoc2json import libdoc2json


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print(f'Usage: python -m libdoc2json <LIBRARY or *.robot or *.py> <Outputfile.json>!\n'
              f'Example: python -m libdoc2json SeleniumLibrary SeleniumLibrary4.0.json\n'
              f'\nArguments: {args}')
    else:
        libdoc(args[0], 'tml_file.xml')
        libdoc2json('tml_file.xml', args[1])
        os.remove('tml_file.xml')


if __name__ == "__main__":
    main()
