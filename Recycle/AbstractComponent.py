'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from abc import ABC, abstractmethod

class AbstractElectrolyser(ABC):
    
    @abstractmethod
    def getEfficiency(self, power):
        pass
    
    @abstractmethod
    def getPower(self, current_density):
        # MW
        pass
    
    @abstractmethod
    def getHeat(self, power):
        # MW
        pass
    
    @abstractmethod
    def getHydrogenProductionRate(self):
        # kg/h
        pass
    
    @abstractmethod
    def getWorkingRange(self) -> tuple:
        '''

        :return: (Minimal current density, Maximal current density)
        '''
        pass
    
class AbstractStorage(ABC):

    @abstractmethod
    def getUpperBound(self):
        # ?% capacity
        pass
    
    @abstractmethod
    def getLowerBound(self):
        # ?% capacity
        pass
    
    @abstractmethod
    def getCapacity(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

class AbstractWindTurbine(ABC):

    @abstractmethod
    def getPower(self, wind_speed):
        # MW
        pass

class AbstractPV(ABC):

    @abstractmethod
    def getPower(self):
        #MW
        pass

class AbstractCompressor(ABC):

    @abstractmethod
    def getPowerToMassFlowRate(self):
        '''

        :return: MW/kg/h
        '''
        pass