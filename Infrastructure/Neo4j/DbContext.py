#https://neo4j.com/developer/python/
from py2neo import Graph, data

from Domain.Enums.Neo4jEnum import Neo4jEnum
from Domain.Interfaces.IContext import IContext
class DbContext(IContext):

    __GraphObject = Graph(f"{Neo4jEnum.DbPrefix}://{Neo4jEnum.DbHost}:{Neo4jEnum.DbPort}", auth=(f"{Neo4jEnum.DbUser}", f"{Neo4jEnum.DbPass}"))
    # __arrQuery:list = ["","",""]
        
    def __init__(self):
        pass

    def Where(self, cWhere:str):
        return " WHERE " + cWhere

    def Select(self, cReturn:str):
        return " RETURN " + cReturn
    
    def ToList(self,arrQuery:str):
        return self.__GraphObject.run(arrQuery).data()

    def First(self,arrQuery:str):
        return self.__GraphObject.run(arrQuery).data()[0]
