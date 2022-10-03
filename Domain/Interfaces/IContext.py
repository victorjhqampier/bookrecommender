from abc import ABCMeta
from abc import abstractmethod

class IContext(metaclass=ABCMeta):
    @abstractmethod
    def Where(self, cWhere:str):
        pass       

    @abstractmethod
    def Select(self, cReturn:str):
        pass
    @abstractmethod
    def ToList(self,arrQuery:str):
        pass

    @abstractmethod
    def First(self,arrQuery:str):
        pass