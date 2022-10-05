from abc import ABCMeta
from abc import abstractmethod

class IPublisher(metaclass=ABCMeta):
    @abstractmethod 
    def MergePublisher(self, arrAuthor:list):
        pass
