from abc import ABCMeta
from abc import abstractmethod

class IHelper(metaclass=ABCMeta):

    @abstractmethod
    def GenerateIdentifier(self, cString:str)->str:
        pass

    @abstractmethod
    def GenerateIndex(self, cString:str)->str:
        pass

    @abstractmethod
    def FormateText(self, cString:str)-> str:
        pass