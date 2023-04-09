from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity

class IPublisher(metaclass=ABCMeta):
    @abstractmethod 
    def MergePublisher(self, arrAuthor:list):
        pass

    @abstractmethod 
    def GetPublisher(self, idTitle:int)->list[PublisherDataEntity]:
        pass
