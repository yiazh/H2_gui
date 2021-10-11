'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from abc import ABC, abstractmethod

class AbstractPtXSystem(ABC):

    @abstractmethod
    def addComponent(self, str:str, obj):
        pass

    @abstractmethod
    def setName(self):
        pass


