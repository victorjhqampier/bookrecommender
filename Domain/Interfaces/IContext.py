from abc import ABCMeta
from abc import abstractmethod

class IContext(metaclass=ABCMeta):
    @abstractmethod
    def Query(self, cQuery:str):
        pass       

    @abstractmethod
    def Where(self, cWhere:str):
        pass

    @abstractmethod
    def Select(self, cReturn:str):
        pass

    @abstractmethod
    def ToList(self):
        pass

    @abstractmethod
    def FirstOrDefault(self):
        pass