from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Data.CopyDataEntity import CopyDataEntity

class ICopy(metaclass=ABCMeta):
    @abstractmethod
    def MergeCopies(self, arrCopies: list):
        pass

    @abstractmethod
    def GetCopy(self, idTitle:int)->list[CopyDataEntity]:
        pass
