#https://neo4j.com/developer/python/
from py2neo import Graph

from Domain.Enums.Neo4jEnum import Neo4jEnum
from Domain.Interfaces.IContext import IContext
from multipledispatch import dispatch


class DbContext(IContext):

    __GraphObject = Graph(f"{Neo4jEnum.DbPrefix}://{Neo4jEnum.DbHost}:{Neo4jEnum.DbPort}", auth=(f"{Neo4jEnum.DbUser}", f"{Neo4jEnum.DbPass}"))    
        
    def __init__(self):
        self.arrQuery:list = ["","","","","",""]#1:query ; 2: Select : las FirstOrDefault()
        self.cAlias:str = ""
    
    def Node(self):        
        return DbContext()

    def Relationship(self):        
        return DbContext()
        
    def Match(self, cNode:str, cKey:str):
        self.cAlias = "ii"
        self.arrQuery[0] += f"MATCH ({self.cAlias}:{cNode}"+"{identity_at:'"+cKey+"'})"
        return self

    @dispatch(str,str,str)
    def Merge(self, cAlias:str,cNode:str, cKey:str):
        self.cAlias = cAlias
        self.arrQuery[0] += f"MERGE ({cAlias}:{cNode}"+"{identity_at:'"+cKey+"'})"
        return self

    @dispatch(int,str,int)
    def Merge(self, idNodeFrom:int,cRelationShip:str, idNodeTo:int):
        self.arrQuery[0] = "MATCH"
        self.arrQuery[2] = "WHERE"

        arrWhere:set = set(self.arrQuery[3].replace(" ",'').split("AND")) if len(self.arrQuery[3]) > 0 else set()
        arrWhere.add(f"ID(r{idNodeFrom})={idNodeFrom}".replace(" ",''))
        arrWhere.add(f"ID(r{idNodeTo})={idNodeTo}".replace(" ",''))
        self.arrQuery[3] = " AND ".join(arrWhere)

        arrMatch:set = set(self.arrQuery[1].replace(" ",'').split(",")) if len(self.arrQuery[1]) > 0 else set()        
        arrMatch.add(f"(r{idNodeFrom})".replace(" ",''))
        arrMatch.add(f"(r{idNodeTo})".replace(" ",''))       
        self.arrQuery[1] = ",".join(arrMatch)

        arrMerge:set = set(self.arrQuery[4].replace(" ",'').split("MERGE")) if len(self.arrQuery[1]) > 0 else set()
        arrMerge.add(f"(r{idNodeFrom})-[:{cRelationShip}]->(r{idNodeTo})".replace(" ",''))        
        self.arrQuery[4] = " MERGE ".join(arrMerge)

        return self
    
    @dispatch(int,str,int,tuple)
    def Merge(self, idNodeFrom:int,cRelationShip:str, idNodeTo:int, tParams:tuple):
        self.arrQuery[0] = "MATCH"
        self.arrQuery[2] = "WHERE"

        arrWhere:set = set(self.arrQuery[3].replace(" ",'').split("AND")) if len(self.arrQuery[3]) > 0 else set()
        arrWhere.add(f"ID(r{idNodeFrom})={idNodeFrom}".replace(" ",''))
        arrWhere.add(f"ID(r{idNodeTo})={idNodeTo}".replace(" ",''))
        self.arrQuery[3] = " AND ".join(arrWhere)

        arrMatch:set = set(self.arrQuery[1].replace(" ",'').split(",")) if len(self.arrQuery[1]) > 0 else set()        
        arrMatch.add(f"(r{idNodeFrom})".replace(" ",''))
        arrMatch.add(f"(r{idNodeTo})".replace(" ",''))       
        self.arrQuery[1] = ",".join(arrMatch)

        tempt:str = "{"+tParams[0] +":'"+tParams[1]+"'}"  
        arrMerge:set = set(self.arrQuery[4].replace(" ",'').split("MERGE")) if len(self.arrQuery[1]) > 0 else set()
        arrMerge.add(f"(r{idNodeFrom})-[:{cRelationShip}{tempt}]->(r{idNodeTo})".replace(" ",''))        
        self.arrQuery[4] = " MERGE ".join(arrMerge)

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
    
    def Where(self, cWhere:str):
        self.arrQuery[1] = f"WHERE {cWhere}"
        return self

    def Select(self, cSelect:str):
        self.arrQuery[5] = f"RETURN {cSelect}"
        return self

    def ToList(self):
        return self.__GraphObject.run(" ".join(self.arrQuery)).data()

    def FirstOrDefault(self):
        result = self.__GraphObject.run(" ".join(self.arrQuery)).data()
        return result[0] if len(result) > 0 else None
    
    def ToString(self):
        return " ".join(self.arrQuery)
