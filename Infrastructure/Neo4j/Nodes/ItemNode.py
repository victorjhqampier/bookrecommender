from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Enums.NodeEnum import NodeEnum
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.IItem import IItem
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class ItemNode(IItem):

    def __init__(self):
        self.__db: IContext = DbContext()
        self.__helper: IHelper = HelperCommon()
        self.__cName: str = NodeEnum.Item
        self.__cAlias:str = "i"
    
    def GetItem(self,objItem: ItemDataEntity,cMoreDescription:str = "") -> str:
        cIdentity = self.__helper.GenerateIdentifier(f"{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.nReleased} {objItem.cType} {cMoreDescription}")
        arrNodeSelect = self.__db.Node().Match(NodeEnum.Item, cIdentity)
        cAlias = arrNodeSelect.cAlias
        arrNodeSelect.Select(f"ID({cAlias}) AS idItem")
        result = arrNodeSelect.FirstOrDefault()
        return result["idItem"] if result is not None else result

    def CreateItem(self, objItem: ItemDataEntity, cMoreDescription:str = ""):
               
        cIdentity: str = ""       
        arrNodeSaving = self.__db.Node()      
        
        if(objItem.cTitle == ''):
            raise Exception("cTitle no puede estar vacio.")

        cIdentity = self.__helper.GenerateIdentifier(f"{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.nReleased} {cMoreDescription}")
        
        cIndex = self.__helper.GenerateIndex(f'{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.nReleased} {objItem.cContent} {objItem.cNotes} {objItem.cTopics}')
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
                        #"cPhysicalDescription" : self.__helper.FormateText(objItem.cPhysicalDescription),
                        "cTopics" : self.__helper.FormateText(objItem.cTopics),
                        "cType" : self.__helper.FormateText(objItem.cType),
                        "cImage" : self.__helper.FormateText(objItem.cImage),
                        #"cLink" : self.__helper.FormateText(objItem.cLink),
                        "nViews" : 0,               
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                ).Merge("dh","Header", "ax"+cIdentity
                ).OnCreate(
                    {
                        "index_at": cIndex,                                 
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).Select(f"ID ({self.__cAlias}) AS idItem, id(dh) AS idHeader")
        
        result = arrNodeSaving.FirstOrDefault()

        NewRelation = self.__db.Relationship().Merge(result['idHeader'],"INDEX", result['idItem'] ).Select('True as idHeader')
        NewRelation.FirstOrDefault()
        
        objItem.idItem = result['idItem']
        return objItem
    
    def GetTitle(self, idTitle:int)->ItemDataEntity:
        BuildToGetTitle= self.__db.Query()
        BuildToGetTitle.Match(            
            ).Node("Title","m"
            ).Where(            
                ).Id("m", idTitle           
            ).Select("ID(m) AS idTitle,m.cTitle AS cTitle,m.cSubtitle AS cSubtitle,m.cEdition AS cEdition,m.nReleased AS nReleased,m.cContent AS cContent,m.cIsbn AS cIsbn,m.cNotes AS cNotes,m.cTopics AS cTopics,m.cType AS cType,m.cImage AS cImage,m.updated_at AS dUpdated")
                    
        return BuildToGetTitle.FirstOrDefault()
