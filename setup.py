'''
Created on Jul 25, 2014

@author: lwoydziak
'''
from setuptools import setup
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

import os.path

if os.path.exists('README.md'):
    import shutil
    shutil.copyfile('README.md', 'README.txt')


setup(name='singleton3',
      version='1.0',
      maintainer='Luke Woydziak',
      maintainer_email='lwoydziak@gmail.com',
      url = 'https://github.com/Pipe-s/singleton3',
      download_url = 'https://github.com/Pipe-s/singleton3/tarball/1.0',
      platforms = ["any"],
      description = 'Python package for making object a Singleton.',
      long_description = read('README.txt'),
      classifiers = [
            'Development Status :: 3 - Alpha',
            'Natural Language :: English',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Unix Shell',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=[
                'singleton3'
               ]
      )

