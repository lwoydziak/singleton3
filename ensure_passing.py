'''
Created on May 2, 2012

@author: lwoydziak
'''

import sys
import argparse
import re

__version__ = '0.2.0'
__all__ = ['', 'main']

def passed(message):
    print ("[PASS] %s" % message)
    return 0

def failed(message):
    print ("[FAIL] %s" % message)
    return 1

def duplication(inputfile, requirement):
    regex = re.compile('.*Clones detected:(.[0-9]+)') # regex to matches the numbers after "Clones detected:"
    for _, line in enumerate(inputfile, start=1):
        matches = regex.match(line)
        if matches is None:
            continue
        duplications = int(matches.group(1))
        if duplications > int(requirement):
            return failed("Copy/Paste detected %s times (allowance %s)"%(duplications, requirement))
        else:
            return passed("Copy/Paste at %s, which is at or below allowance of %s"%(duplications, requirement))
    return passed("Copy/Paste at $errors, which is at or below allowance of %s"%(requirement));

def complexity(inputfile, requirement): 
    regex = re.compile('.*complexity\":(.[0-9]+)') # regex to matches the numbers after "complexity" :
    for _, fileline in enumerate(inputfile, start=1):
        newlines = fileline.replace(',', "\n")
        outputlist = newlines.splitlines()
        for line in outputlist:
            matches = regex.match(line)
            if matches is None:
                continue
            complexityScore = int(matches.group(1))
            if complexityScore > int(requirement):
                return failed("Complexity detected %s (allowance %s)"%(complexityScore, requirement))
            else:
                continue
        return passed("All complexity scores at or below allowance of %s"%(requirement));

build_steps = {"duplication" : duplication, "complexity" : complexity}

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    commandLine = argparse.ArgumentParser(description='Check for build target passing')
    commandLine.add_argument('--version', action='version', version="%(prog)s "+__version__)
    commandLine.add_argument('--build_step', type=str, help='build step to analyze', required=True, choices=build_steps.keys())
    commandLine.add_argument('--threshold', type=int, help='Threshold for the build step', required=False, default="0")
    commandLine.add_argument('inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    environment = commandLine.parse_args(argv)

    return build_steps[environment.build_step](environment.inputfile, environment.threshold)
   
if __name__ == '__main__':
    if sys.argv[0] is None:
        # fix for weird behaviour when run with python -m
        # from a zipped egg.
        sys.argv[0] = 'ensure_passing.py'
    sys.exit(main())


