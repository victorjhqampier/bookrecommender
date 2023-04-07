from abc import ABCMeta
from abc import abstractmethod
from multipledispatch import dispatch

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
    def Merge(self, idNodeFrom:int,cRelationShip:str, idNodeTo:int):
        pass

    @abstractmethod
    def Merge(self, idNodeFrom:int,cRelationShip:str, idNodeTo:int, tParams:tuple):
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

    #Nueva implemetacion
    @abstractmethod
    def Query(self):
        pass
    
    @abstractmethod
    
    def Match(self):
        pass

    @abstractmethod
    def Node(self, cNode:str, cAlias:str):
        pass

    @abstractmethod
    def LeftRelationship(self, cRelationship:str, cAlias:str = ""):
        pass

    @abstractmethod
    def RightRelationship(self, cRelationship:str, cAlias:str = ""):
        pass

    @abstractmethod
    def As(self, cAlias:str):
        pass

    @abstractmethod    
    def Where(self):
        pass

    @abstractmethod
    def Id(self, cNode:str,IdNode:int):
        pass

    @abstractmethod
    def And(self, cNode:str = ""):
        pass

    @abstractmethod    
    def With(self):
        pass

    @abstractmethod
    def Node(self, cAlias:str):
        pass

    @abstractmethod
    def Count(self, cAlias:str):
        pass

    @abstractmethod
    def OnSet(self, cNodeTo:str, cRelationship:str, cNodeFrom:str, IdNode:str):
        pass

    @abstractmethod
    def FromRaw(self,cQuery:str):
        pass

    @abstractmethod
    def StartWith(self, cStartWith:str=""):
        pass

    @abstractmethod
    def Substring(self, cNode:str, nLong:int):
        pass

    @abstractmethod
    def OrderByDescending(self, cNode:str):
        pass
    
    @abstractmethod
    def Limit(self, nLimit:int):
        pass

    @abstractmethod
    def SearchByIndex(self,cKeyWord:str,cIndex:str):
        pass
    
    @abstractmethod
    def SortObjectCollect(self,cObject:str,cOrderBy:str):
        pass
    
    @abstractmethod
    def CountId(self,cNode:str):
        pass