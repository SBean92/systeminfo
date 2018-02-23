'''
Setup File for systeminfo
Created on 20th Feb 2018 in Visual Studio Code

@author: SBean
'''
from setuptools import setup

setup(
    name = "systeminfo",
    version = "0.1",
    description = "Basic system information for COMP30670",
    url="https://github.com/SBean92/systeminfo",
    author = "Sean Behan",
    aurhor_email = "sean.behan@ucdconnect.ie",
    licence = "GPL3",
    packages = ['systeminfo'],
    entry_points = {
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
    }
)
