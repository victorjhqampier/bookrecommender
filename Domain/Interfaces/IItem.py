from abc import ABCMeta
from abc import abstractmethod
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity

class IItem(metaclass=ABCMeta):
    @abstractmethod
    def GetItem(self,objItem: ItemDataEntity)->str:
        pass
    @abstractmethod
    def CreateItem(self, objItem: ItemDataEntity,cMoreDescription:str = ""):
        pass

    @abstractmethod
    def GetTitle(self, idTitle:int)->ItemDataEntity:
        pass
