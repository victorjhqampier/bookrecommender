from abc import ABCMeta
from abc import abstractmethod
class IAutenticacion(metaclass=ABCMeta):
    
    @abstractmethod 
    def IniciarSesion(self,user:str,paswd:str):        
        pass
    
    @abstractmethod     
    def VerificarIdUsuario(self,idUsuario:int):        
        pass