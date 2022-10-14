from abc import ABCMeta
from abc import abstractmethod

class IContext(metaclass=ABCMeta):
    @abstractmethod
    def Node(self):
        pass       

    @abstractmethod
    def Relationship(self):
        pass

    @abstractmethod
    def Merge(self, cAlias:str,cNode:str, cKey:str):
        pass

    @abstractmethod
    def OnCreate(self, cDict:dict):
        pass

    @abstractmethod
    def OnMatch(self, cDict:dict):
        pass

    @abstractmethod
    def Where(self, cWhere:str):
        pass

    @abstractmethod
    def Select(self, cSelect:str):
        pass

    @abstractmethod
    def ToList(self):
        pass

    @abstractmethod
    def FirstOrDefault(self):
        pass

    @abstractmethod
    def ToString(self):
        pass