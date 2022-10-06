from abc import ABCMeta
from abc import abstractmethod
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity

class ISerialTitle(metaclass=ABCMeta):
    @abstractmethod 
    def MergeSerialTitle(self, objSerialTitle: SerialTitlesDataEntity):
        pass
