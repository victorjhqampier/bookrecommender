from abc import ABCMeta
from abc import abstractmethod

class IAuthor(metaclass=ABCMeta):
    @abstractmethod 
    def MergeAuthors(self, arrAuthor:list):
        pass
