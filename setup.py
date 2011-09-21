from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='PyFakeMail',
      version=version,
      description="Fake Mail Server",
      long_description=open('README').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Pedro Bur\xc3\xb3n',
      author_email='pedro@witoi.com',
      url='http://PyFakeMail.github.com',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      test_suite='tests',
      tests_require=[
        'mock',
      ],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts': [
            'pyfakemail = fakemail:main',
        ]
      },
      )
