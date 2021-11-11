'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from AbstractPtX import AbstractPtXSystem

class GLS_system(AbstractPtXSystem):

    def __init__(self):
        self.components = {}

    def addComponent(self, str:str, obj):
        self.components[str] = obj
        pass

    def setName(self):
        self.name = 'GreenLab Skive project'
