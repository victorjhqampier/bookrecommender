from abc import ABCMeta
from abc import abstractmethod
from Domain.Entities.Data.BookSimpleEntity import BookSimpleEntity

class IRecomInfrastructure(metaclass=ABCMeta):
    
    @abstractmethod 
    def SearchBook(self,cKeyWord:str) -> list[BookSimpleEntity]:
        pass
    
    @abstractmethod
    def GetJaccardIndexRecom(self,idTitle:int) -> list[BookSimpleEntity]:
        pass

    @abstractmethod
    def GetCoResponsibilityRecom(self,idTitle:int) -> list[BookSimpleEntity]:
        pass

    @abstractmethod
    def GetClassificationRecom(self,idTitle:int) -> list[BookSimpleEntity]:
        pass