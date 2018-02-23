'''
Main function for systeminfo
Created on 20th Feb 2018 in Visual Studio Code

@author: SBean92
'''
import platform

def getPlat():
    return platform.platform()

def getProcessor():
    if platform.processor == "":
        return "No processor info found"
    else:
        return platform.processor()

def getSystem():
    if platform.system == "":
        return "No platform information found"
    else:
        return platform.system()
