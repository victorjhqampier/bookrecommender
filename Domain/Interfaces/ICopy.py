from abc import ABCMeta
from abc import abstractmethod

class ICopy(metaclass=ABCMeta):
    @abstractmethod 
    def MergeCopies(self, arrCopies: list):
        pass
