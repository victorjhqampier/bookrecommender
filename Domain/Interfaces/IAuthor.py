from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity

class IAuthor(metaclass=ABCMeta):
    @abstractmethod 
    def MergeAuthors(self, arrAuthor:list):
        pass

    @abstractmethod
    def GetAuthor(self, idTitle:int)->list[AuthorDataEntity]:
        pass
