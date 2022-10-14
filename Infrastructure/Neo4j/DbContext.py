#https://neo4j.com/developer/python/
from py2neo import Graph, data

from Domain.Enums.Neo4jEnum import Neo4jEnum
from Domain.Interfaces.IContext import IContext

class DbContext(IContext):

    __GraphObject = Graph(f"{Neo4jEnum.DbPrefix}://{Neo4jEnum.DbHost}:{Neo4jEnum.DbPort}", auth=(f"{Neo4jEnum.DbUser}", f"{Neo4jEnum.DbPass}"))    
        
    def __init__(self):
        self.arrQuery:list = ["","","","","",""]#1:query ; 2: Select : las FirstOrDefault()
        self.cAlias:str = ""
    # @staticmethod
    # def Graph():
    #     return DbContext()

    # def Query(self, cQuery:str):
    #     self.arrQuery[0] = cQuery
    #     return DbContext()
    def Node(self):
        return DbContext()

    def Relationship(self):
        return DbContext()

    def Merge(self, cAlias:str,cNode:str, cKey:str):
        self.cAlias = cAlias
        self.arrQuery[0] += f"MERGE ({cAlias}:{cNode}"+"{identity_at:'"+cKey+"'})"
        return self
        # return DbContext()
    def MergeRelation(self, cAlias:str,idNodeFrom:str, cRelation:str, idNodeTo:str, cKey:str = None):
        self.cAlias = cAlias
        tempt:str = "{identity_at:'"+cKey+"'})" if cKey is not None else ""
        self.arrQuery[0] += f"MERGE ({idNodeFrom})-[{self.cAlias}:{cRelation}{tempt}]->({idNodeTo})"
        return self

    def Merges(self, idNodeFrom:str,cRelationShip:str, idNodeTo:str, tParams:tuple = None):
        srdr = "MATCH (n), (m) where id(n) = 5 and id(m) = 4"
        esrt = "MERGE (n)-[:AUTHOR{rol: 'Autor'}]->(m)"
        self.cAlias = cAlias
        self.arrQuery[0] += f"MERGE ({cAlias}:{cNode}"+"{identity_at:'"+cKey+"'})"
        return self
        
    
    def OnCreate(self, cDict:dict):
        self.arrQuery[0] += f" ON CREATE SET "        
        temp:list = []
        for item in cDict.keys():
            temp.append(
                f"{self.cAlias}.{item}=" +
                str(f"'{cDict[item]}'" if not isinstance(cDict[item], int) else f"{cDict[item]}")
            )
        self.arrQuery[0] += ",".join(temp) + " "
        return self

    def OnMatch(self, cDict:dict):
        self.arrQuery[0] += f"ON MATCH SET "        
        temp:list = []
        for item in cDict.keys():
            temp.append(
                f"{self.cAlias}.{item}=" +
                str(f"'{cDict[item]}'" if not isinstance(cDict[item], int) else f"{cDict[item]}")
            )
        self.arrQuery[0] += ",".join(temp) + " "
        return self
    
    # def OnCreate(self, cWhere:str):
    #     self.arrQuery[1] = f"WHERE {cWhere}"
    #     return self
    
    # def Match(self, cQuery:str):
    #     self.arrQuery[0] = cQuery
    #     return DbContext()
    
    # def Create(self, cQuery:str):
    #     self.arrQuery[0] = cQuery
    #     return DbContext()

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
    
    def ToString(self):
        return "".join(self.arrQuery)
