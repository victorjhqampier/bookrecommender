from abc import ABCMeta
from abc import abstractmethod
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity

class IClassification(metaclass=ABCMeta):
    @abstractmethod 
    def MergeClassification(self, objClassification: ClassificationDataEntity):
        pass
