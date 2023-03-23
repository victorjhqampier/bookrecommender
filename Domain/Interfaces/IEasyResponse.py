from abc import ABCMeta
from abc import abstractmethod

from Domain.Entities.Response import Response

class IEasyResponse(metaclass=ABCMeta):
    @abstractmethod 
    def EasyErrorRespond(self,cErrorCode:str, cErrorMessage:str, cMessage:str = None)->Response:
        pass

    @abstractmethod
    def EasyListErrorRespond(self,errorList, cMessage:str = None)->Response:
        pass

    @abstractmethod
    def EasyEmptyRespond(self,cMessage:str = None)->Response:
        pass

    @abstractmethod
    def EasySuccessRespond(self,dataResponse, cMessage:str = None)->Response:
        pass