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
    __cReturn: str = "ID (i) AS idItem"

    def __init__(self):
        pass

    def CreateItem(self, objItem: ItemDataEntity):
               
        cIdentity: str = ""
        cNodeHeader: str = ""
        cQuery: str = ""        
        
        if(objItem.cTitle == ''):
            raise Exception("cTitle no puede estar vacio.")
        
        cIdentity = self.__helper.GenerateIdentifier(f"{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.nReleased} {objItem.cType}")
        cIndex = self.__helper.GenerateIndex(f'{objItem.cIsbn} {objItem.cTitle} {objItem.cSubtitle} {objItem.cEdition} {objItem.cContent} {objItem.cNotes} {objItem.cTopics} {objItem.cPhysicalDescription}')
        cQuery = "CREATE (i:Item{"\
                f"cTitle :'{self.__helper.FormateText(objItem.cTitle)}',"\
                f"cSubtitle :'{self.__helper.FormateText(objItem.cSubtitle)}',"\
                f"cEdition :'{self.__helper.FormateText(objItem.cEdition)}',"\
                f"nReleased :{objItem.nReleased},"\
                f"cContent :'{self.__helper.FormateText(objItem.cContent)}',"\
                f"cIsbn :'{self.__helper.FormateText(objItem.cIsbn)}',"\
                f"cNotes :'{self.__helper.FormateText(objItem.cNotes)}',"\
                f"cPhysicalDescription :'{self.__helper.FormateText(objItem.cPhysicalDescription)}',"\
                f"cTopics :'{self.__helper.FormateText(objItem.cTopics)}',"\
                f"cType :'{self.__helper.FormateText(objItem.cType)}',"\
                f"cImage :'{self.__helper.FormateText(objItem.cImage)}',"\
                f"cLink :'{self.__helper.FormateText(objItem.cLink)}',"\
                f"nViews :0,"\
                f"identity_at :'{cIdentity}',"\
                f"status_at:true,"\
                f"updated_at:'{str(datetime.now())}',"\
                f"created_at:'{str(datetime.now())}'"\
                "})"\
                "CREATE (h:Head{index_at:"\
                "'"+cIndex+"'}) "\
                "CREATE (h)-[:BODY]->(i)"
        cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)
                
        objIdSerial = self.__db.First(cNodeHeader)
        objItem.idItem = objIdSerial['idItem']

        return objItem
