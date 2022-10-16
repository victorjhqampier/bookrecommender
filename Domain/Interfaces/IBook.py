from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity

class IBook(metaclass=ABCMeta):
    @abstractmethod 
    def SaveBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        pass

    @abstractmethod 
    def SaveBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        pass

    @abstractmethod 
    def UpdateBook (self, objItem:ItemDataEntity, arrCopies:list):
        pass
