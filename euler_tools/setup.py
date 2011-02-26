from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='euler_tools',
      version=version,
      description="Helper for Project Euler problems",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='project euler helper',
      author='dummy3k',
      author_email='l4711@gmx.net',
      url='https://github.com/dummy3k/Project-Euler',
      license='',
      #~ py_modules = ['misc'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
