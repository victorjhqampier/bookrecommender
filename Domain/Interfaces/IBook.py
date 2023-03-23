from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Request.MergeBookResponseEntity import MergeBookResponseEntity

class IBook(metaclass=ABCMeta):

    @abstractmethod 
    def MergeBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity)-> MergeBookResponseEntity:
        pass
