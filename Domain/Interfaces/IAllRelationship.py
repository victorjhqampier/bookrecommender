from abc import ABCMeta
from abc import abstractmethod
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity

from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity

class IAllRelationship(metaclass=ABCMeta):
    @abstractmethod 
    def MergeAllRelationships(self, objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:list, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        pass