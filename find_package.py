import sys
import argparse
import re
import operator
from distutils.version import LooseVersion

__version__ = '0.2.0'
__all__ = ['', 'main']

def passed(message):
    #print (message)
    return 0

def install(message):
    print (message)
    return 1

def upgrade(message):
    print (message)
    return 2

ops = {'>':operator.gt, '>=' : operator.ge, '=':operator.eq, '==':operator.eq}

def checkForPackage(inputfile, package):
    breakout = re.search("([a-z]+)([\=\>]+)([0-9.]*)", package)
    version = None
    if breakout:
        package = breakout.group(1)
        operation = breakout.group(2)
        version = breakout.group(3)
    regex = re.compile('^'+package+'==(.*)') # regex to matches the package name at the beginning of the line
    for _, line in enumerate(inputfile, start=1):
        matches = regex.match(line)
        if matches is None:
            continue
        package_installed_version = matches.group(1)
        if version is None:
            return passed(package + "@" +package_installed_version + " found")        
        if ops[operation](LooseVersion(package_installed_version), LooseVersion(version)):
            return passed(package+"@"+package_installed_version+" found.")
        else:
            return upgrade(package+" installed, but "+package_installed_version+" not "+operation+" "+version+".")
    return install(package+" not installed.");


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    commandLine = argparse.ArgumentParser(description='Check for Python package')
    commandLine.add_argument('--version', action='version', version="%(prog)s "+__version__)
    commandLine.add_argument('--package', type=str, help='package to look for (use package==level to specify level)', required=True)
    commandLine.add_argument('inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    environment = commandLine.parse_args(argv)

    return checkForPackage(environment.inputfile, environment.package)

if __name__ == '__main__':
    if sys.argv[0] is None:
        # fix for weird behaviour when run with python -m
        # from a zipped egg.
        sys.argv[0] = 'find_package.py'
    sys.exit(main())

