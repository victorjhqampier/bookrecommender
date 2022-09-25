from abc import ABCMeta
from abc import abstractmethod

class IEasyResponse(metaclass=ABCMeta):
    @abstractmethod 
    def EasyErrorRespond(self,cErrorCode:str, cErrorMessage:str, cMessage:str = None):
        pass

    @abstractmethod
    def EasyListErrorRespond(self,errorList, cMessage:str = None):
        pass

    @abstractmethod
    def EasyEmptyRespond(self,cMessage:str = None):
        pass

    @abstractmethod
    def EasySuccessRespond(self,dataResponse, cMessage:str = None):
        pass