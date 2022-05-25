#!/usr/bin/env python3

from setuptools import setup

setup(name='piip',
      version='0.2',
      description='Get private IP sent per SMS',
      author='David Rieger',
      author_email='david@isan.engineer',
      url='https://github.com/frontside/piip.git',
      packages=['piip'],
      entry_points={
          'console_scripts': [
              'piip = piip.__main__:main'
          ]
      },
      data_files=[
          ("/etc", ['piip/piipconf.yaml'])
      ],
      install_requires=[
          "certifi==2017.7.27.1",
          "chardet==3.0.4",
          "idna==2.6",
          "netifaces==0.10.6",
          "PyJWT==2.4.0",
          "PySocks==1.6.7",
          "pytz==2017.2",
          "requests==2.20.0",
          "six==1.11.0",
          "twilio==6.8.2",
          "urllib3==1.24.2",
          "PyYAML==5.1"
      ])
