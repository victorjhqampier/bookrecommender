from abc import ABCMeta
from abc import abstractmethod

class ICryptography(metaclass=ABCMeta):
    @abstractmethod 
    def CrearPassword(self):
        pass
    @abstractmethod 
    def ProbarPassword(self):
        pass
    @abstractmethod    
    def CifrarCadena(self,cCadena:str, cKey:str):
        pass
    @abstractmethod 
    def DescifrarCadena(self, cCadena:str, cKey:str):
        pass