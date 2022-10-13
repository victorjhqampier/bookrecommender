#https://neo4j.com/developer/python/
from py2neo import Graph, data

from Domain.Enums.Neo4jEnum import Neo4jEnum
from Domain.Interfaces.IContext import IContext

class DbContext(IContext):

    __GraphObject = Graph(f"{Neo4jEnum.DbPrefix}://{Neo4jEnum.DbHost}:{Neo4jEnum.DbPort}", auth=(f"{Neo4jEnum.DbUser}", f"{Neo4jEnum.DbPass}"))    
        
    def __init__(self):
        self.arrQuery:list = ["","","","","",""]#1:query ; 2: Select : las FirstOrDefault()
    # @staticmethod
    # def Graph():
    #     return DbContext()

    def Query(self, cQuery:str):
        self.arrQuery[0] = cQuery
        return DbContext()

    def Where(self, cWhere:str):
        self.arrQuery[1] = f"WHERE {cWhere}"
        return self

    def Select(self, cSelect:str):
        self.arrQuery[5] = f"RETURN {cSelect}"
        return self
    
    def ToList(self):
        return self.__GraphObject.run(" ".join(self.arrQuery)).data()

    def FirstOrDefault(self):
        return self.__GraphObject.run(" ".join(self.arrQuery)).data()[0]
