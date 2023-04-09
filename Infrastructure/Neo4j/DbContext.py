#https://neo4j.com/developer/python/
from py2neo import Graph

from Domain.Enums.Neo4jEnum import Neo4jEnum
from Domain.Interfaces.IContext import IContext
from multipledispatch import dispatch


class DbContext(IContext):

    __GraphObject = Graph(f"{Neo4jEnum.DbPrefix}://{Neo4jEnum.DbHost}:{Neo4jEnum.DbPort}", auth=(f"{Neo4jEnum.DbUser}", f"{Neo4jEnum.DbPass}"))    
        
    def __init__(self):
        self.arrQuery:list = ["","","","","","",""]#1:query ; 2: Select : las FirstOrDefault()
        self.cAlias:str = ""
        self.nElement:int=-1

        # self.arrMatch:list=[]
        # self.arrWith:list=[]
        # self.arrCollect:list=[]
        # self.arrSet:list=[]
    @dispatch()
    def Node(self):        
        return DbContext()

    def Relationship(self):        
        return DbContext()

    @dispatch(str,str)    
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
    
    @dispatch(str)
    def Where(self, cWhere:str):
        if(self.arrQuery[1] == ""):
            self.arrQuery[1] = f"WHERE {cWhere}"
        else:
            self.arrQuery[self.nElement] += f" WHERE {cWhere}"
        return self

    def Select(self, cSelect:str):
        # self.arrQuery[5] = f"RETURN {cSelect}"
        self.arrQuery[-1] += f" RETURN {cSelect}"
        return self

    def ToList(self):
        self.arrQuery = [" ".join(query.split()).strip() for query in self.arrQuery]
        return self.__GraphObject.run(" ".join(self.arrQuery)).data()

    def FirstOrDefault(self):
        self.arrQuery = [" ".join(query.split()).strip() for query in self.arrQuery]
        result = self.__GraphObject.run(" ".join(self.arrQuery)).data()
        return result[0] if len(result) > 0 else None
    
    def ToString(self):
        self.arrQuery = [" ".join(query.split()).strip() for query in self.arrQuery]
        return " ".join(self.arrQuery)
    
# nueva implementacion para consulta
    def Query(self):
        # self.arrQuery = []  
        return DbContext()
    
    @dispatch()
    def Match(self):        
        self.nElement +=1
        self.arrQuery[self.nElement]+="MATCH "
        return self
    
    @dispatch(str,str)
    def Node(self, cNode:str, cAlias:str):
        self.arrQuery[self.nElement]+=f"({cAlias}:{cNode})"
        return self
    
    def LeftRelationship(self, cRelationship:str, cAlias:str = ""):
        self.arrQuery[self.nElement]+=f"<-[{cAlias}:{cRelationship}]-"
        return self
        
    def RightRelationship(self, cRelationship:str, cAlias:str = ""):
        self.arrQuery[self.nElement]+=f"-[{cAlias}:{cRelationship}]->"
        return self
    
    def As(self, cAlias:str):
        self.arrQuery[self.nElement]+=f" AS {cAlias}"
        return self
    
    @dispatch()
    def Where(self):
        self.nElement +=1
        self.arrQuery[self.nElement]+=f"WHERE"
        return self
    
    @dispatch(str,int)
    def Id(self, cNode:str,IdNode:int):
        self.arrQuery[self.nElement]+=f" ID({cNode})={IdNode}"
        return self
    
    # @dispatch(str)
    def And(self, cNode:str = ""):
        self.arrQuery[self.nElement]+=", " if (cNode == "") else f" AND {cNode}"
        return self
    
    @dispatch()
    def With(self):
        self.nElement +=1
        self.arrQuery[self.nElement]+=f"WITH "
        return self
    
    @dispatch(str)
    def Node(self, cAlias:str):
        if(self.arrQuery[self.nElement].strip()[-1]=="-" or self.arrQuery[self.nElement].strip()[-1]==">" or  self.arrQuery[self.nElement].strip()[-2]=="C" or self.arrQuery[self.nElement].strip()[-2]==")"):
            self.arrQuery[self.nElement]+=f"({cAlias})"
        else:
            self.arrQuery[self.nElement]+=f"{cAlias}"
        return self
    
    @dispatch(str)
    def Count(self, cAlias:str):
        self.arrQuery[self.nElement]+=f" COUNT({cAlias})"
        return self
    
    # @dispatch(str)
    def OnSet(self, cNodeTo:str, cRelationship:str, cNodeFrom:str, IdNode:str=""):
        IdNode = IdNode if IdNode != "" else cNodeFrom
        self.arrQuery[self.nElement]+=f"[({cNodeTo})<-[:{cRelationship}]-({cNodeFrom}) | ID({IdNode})]"
        return self
        
    def FromRaw(self,cQuery:str):
        self.arrQuery[self.nElement]+=cQuery
        return self
    
    def StartWith(self, cStartWith:str=""):
        self.arrQuery[self.nElement]+=f" STARTS WITH {cStartWith}"
        return self
    
    def Substring(self, cNode:str, nLong:int):
        self.arrQuery[self.nElement]+=f" SUBSTRING({cNode},0,{nLong})"
        return self
    
    def OrderByDescending(self, cNode:str):        
        cNode = ",".join([n + " DESC" for n in cNode.split(",")])
        self.arrQuery[-1]+=f" ORDER BY {cNode}"
        return self
    
    def Limit(self, nLimit:int):
        self.arrQuery[-1]+=f" LIMIT {nLimit}"
        return self
        
    def SearchByIndex(self,cKeyWord:str,cIndex:str):
        self.nElement +=1
        self.arrQuery[self.nElement]+=f"CALL db.index.fulltext.queryNodes('{cIndex}', '{cKeyWord}') YIELD node MATCH (node)-[]->"
        return self
    
    def SortObjectCollect(self,cObject:str,cOrderBy:str):
        self.arrQuery[self.nElement]+=f"apoc.coll.sortMulti(COLLECT ({cObject}), ['^{cOrderBy}'])[0] "
        return self
    
    def CountId(self,cNode:str):
        self.arrQuery[self.nElement]+=f"COUNT(id({cNode})) "
        return self
    
    def UpdateField(self,cField:str, cValue:str):
        self.arrQuery[self.nElement]+=f" SET {cField}={cValue} "
        return self