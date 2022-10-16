from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Enums.NodeEnum import NodeEnum
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.ISerialTitle import ISerialTitle
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class SerialTitleNode(ISerialTitle):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __cName: str = NodeEnum.SerialTitle
    __cAlias:str = "t"

    def __init__(self):
        pass

    def MergeSerialTitle(self, objSerialTitle: SerialTitlesDataEntity):
               
        cIdentity: str = ""       
        arrNodeSaving = self.__db.Node()       
        
        if(objSerialTitle.cTitle == ''):
            objSerialTitle.idSerialTitle = "0"
            return objSerialTitle
        
        cIdentity = self.__helper.GenerateIdentifier(f"{objSerialTitle.cTitle}")
        arrNodeSaving.Merge(self.__cAlias,self.__cName, cIdentity
                ).OnCreate(
                    {
                        "cTitle":self.__helper.FormateText(objSerialTitle.cTitle.title()),
                        "index_at":self.__helper.GenerateIndex(objSerialTitle.cTitle),
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                ).Select(f"ID ({self.__cAlias}) AS idSerialTitle")
        
        result = arrNodeSaving.FirstOrDefault()
        objSerialTitle.idSerialTitle = result['idSerialTitle']

        return objSerialTitle