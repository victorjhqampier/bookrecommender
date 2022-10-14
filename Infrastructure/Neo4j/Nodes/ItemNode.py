from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.IItem import IItem
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class ItemNode(IItem):

    
    # __cReturn: str = "ID (s) AS idItem"

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __cName: str = "Item"
    __cAlias:str = "i"

    def __init__(self):
        pass
    
    def GetItem(self,itemIdentity:str):
        cQuery:str = "MATCH (s:Item{identity_at:'"+itemIdentity+"'}) return ID(s) AS idItem"
        objIdItem = self.__db.First(cQuery)
        return objIdItem['idItem']

    def CreateItem(self, objItem: ItemDataEntity):
               
        cIdentity: str = ""       
        arrNodeSaving = self.__db.Node()      
        
        if(objItem.cTitle == ''):
            raise Exception("cTitle no puede estar vacio.")

        cIdentity = self.__helper.GenerateIdentifier(f"{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.nReleased} {objItem.cType}")
        cIndex = self.__helper.GenerateIndex(f'{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.cContent} {objItem.cNotes} {objItem.cTopics} {objItem.cPhysicalDescription}')
        arrNodeSaving.Merge(self.__cAlias,self.__cName, cIdentity
                ).OnCreate(
                    {   
                        "cTitle" : self.__helper.FormateText(objItem.cTitle),
                        "cSubtitle" : self.__helper.FormateText(objItem.cSubtitle),
                        "cEdition" : self.__helper.FormateText(objItem.cEdition),
                        "nReleased" : objItem.nReleased,
                        "cContent" : self.__helper.FormateText(objItem.cContent),
                        "cIsbn" : self.__helper.FormateText(objItem.cIsbn),
                        "cNotes" : self.__helper.FormateText(objItem.cNotes),
                        "cPhysicalDescription" : self.__helper.FormateText(objItem.cPhysicalDescription),
                        "cTopics" : self.__helper.FormateText(objItem.cTopics),
                        "cType" : self.__helper.FormateText(objItem.cType),
                        "cImage" : self.__helper.FormateText(objItem.cImage),
                        "cLink" : self.__helper.FormateText(objItem.cLink),
                        "nViews" : 0,               
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                ).Select(f"ID ({self.__cAlias}) AS idItem"
                ).Merge("te","Head", f"ID({self.__cAlias})"
                ).OnCreate(
                    {                        
                        "index_at":cIndex
                    }
                ).MergeRelation("","i","HEAD", "te",None)
                

        return arrNodeSaving.ToString()
        # cNodeHeader = self.__arrComman[0] + f"(s:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
        # cIndex = self.__helper.GenerateIndex(f'{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.cContent} {objItem.cNotes} {objItem.cTopics} {objItem.cPhysicalDescription}')
        # cQuery = f"{self.__arrComman[1]}"\
        #         f"s.cTitle ='{self.__helper.FormateText(objItem.cTitle)}',"\
        #         f"s.cSubtitle ='{self.__helper.FormateText(objItem.cSubtitle)}',"\
        #         f"s.cEdition ='{self.__helper.FormateText(objItem.cEdition)}',"\
        #         f"s.nReleased ={objItem.nReleased},"\
        #         f"s.cContent ='{self.__helper.FormateText(objItem.cContent)}',"\
        #         f"s.cIsbn ='{self.__helper.FormateText(objItem.cIsbn)}',"\
        #         f"s.cNotes ='{self.__helper.FormateText(objItem.cNotes)}',"\
        #         f"s.cPhysicalDescription ='{self.__helper.FormateText(objItem.cPhysicalDescription)}',"\
        #         f"s.cTopics ='{self.__helper.FormateText(objItem.cTopics)}',"\
        #         f"s.cType ='{self.__helper.FormateText(objItem.cType)}',"\
        #         f"s.cImage ='{self.__helper.FormateText(objItem.cImage)}',"\
        #         f"s.cLink ='{self.__helper.FormateText(objItem.cLink)}',"\
        #         f"s.nViews =0,"\
        #         f"s.status_at=true,"\
        #         f"s.updated_at='{str(datetime.now())}',"\
        #         f"s.created_at='{str(datetime.now())}' "\
        #         "MERGE (h:Head{identity_at:ID(s)}) "\
        #         f"ON CREATE SET h.index_at='{cIndex}' "\
        #         "MERGE (h)-[:BODY]->(s)"
        # cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)          
        # objIdItem = self.__db.First(cNodeHeader)
        # objItem.idItem = objIdItem['idItem']
        # return objItem
