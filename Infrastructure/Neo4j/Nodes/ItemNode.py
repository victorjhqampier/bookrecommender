from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.IItem import IItem
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class ItemNode(IItem):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()    
    __arrComman: list = ["MERGE ", " ON CREATE SET ", " ON MATCH SET "]
    __cName: str = "Item"
    __cReturn: str = "ID (s) AS idItem"

    def __init__(self):
        pass
    
    def GetItem(self,itemIdentity:str):
        cQuery:str = "MATCH (s:Item{identity_at:'"+itemIdentity+"'}) return ID(s) AS idItem"
        objIdItem = self.__db.First(cQuery)
        return objIdItem['idItem']

    def CreateItem(self, objItem: ItemDataEntity):
               
        cIdentity: str = ""
        cNodeHeader: str = ""
        cQuery: str = ""        
        
        if(objItem.cTitle == ''):
            raise Exception("cTitle no puede estar vacio.")

        cIdentity = self.__helper.GenerateIdentifier(f"{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.nReleased} {objItem.cType}")
        cNodeHeader = self.__arrComman[0] + f"(s:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
        cIndex = self.__helper.GenerateIndex(f'{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.cContent} {objItem.cNotes} {objItem.cTopics} {objItem.cPhysicalDescription}')
        cQuery = f"{self.__arrComman[1]}"\
                f"s.cTitle ='{self.__helper.FormateText(objItem.cTitle)}',"\
                f"s.cSubtitle ='{self.__helper.FormateText(objItem.cSubtitle)}',"\
                f"s.cEdition ='{self.__helper.FormateText(objItem.cEdition)}',"\
                f"s.nReleased ={objItem.nReleased},"\
                f"s.cContent ='{self.__helper.FormateText(objItem.cContent)}',"\
                f"s.cIsbn ='{self.__helper.FormateText(objItem.cIsbn)}',"\
                f"s.cNotes ='{self.__helper.FormateText(objItem.cNotes)}',"\
                f"s.cPhysicalDescription ='{self.__helper.FormateText(objItem.cPhysicalDescription)}',"\
                f"s.cTopics ='{self.__helper.FormateText(objItem.cTopics)}',"\
                f"s.cType ='{self.__helper.FormateText(objItem.cType)}',"\
                f"s.cImage ='{self.__helper.FormateText(objItem.cImage)}',"\
                f"s.cLink ='{self.__helper.FormateText(objItem.cLink)}',"\
                f"s.nViews =0,"\
                f"s.status_at=true,"\
                f"s.updated_at='{str(datetime.now())}',"\
                f"s.created_at='{str(datetime.now())}' "\
                "MERGE (h:Head{identity_at:ID(s)}) "\
                f"ON CREATE SET h.index_at='{cIndex}' "\
                "MERGE (h)-[:BODY]->(s)"
        cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)          
        objIdItem = self.__db.First(cNodeHeader)
        objItem.idItem = objIdItem['idItem']
        return objItem
