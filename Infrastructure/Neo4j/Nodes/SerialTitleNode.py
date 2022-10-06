from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.ISerialTitle import ISerialTitle
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class SerialTitleNode(ISerialTitle):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __arrComman: list = ["MERGE ", " ON CREATE SET ", " ON MATCH SET "]
    __cName: str = "SerialTitles"
    __cReturn: str = "ID (s) AS idSerialTitle"

    def __init__(self):
        pass

    def MergeSerialTitle(self, objSerialTitle: SerialTitlesDataEntity):
               
        cIdentity: str = ""
        cNodeHeader: str = ""
        cQuery: str = ""        
        
        if(objSerialTitle.cTitle == ''):
            raise Exception("cTitle no puede estar vacio.")
        
        cIdentity = self.__helper.GenerateIdentifier(f"{objSerialTitle.cTitle}")
        cNodeHeader = self.__arrComman[0] + f"(s:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
        cQuery = f"{self.__arrComman[1]}"\
                f"s.cTitle='{self.__helper.FormateText(objSerialTitle.cTitle)}',"\
                f"s.index_at='{self.__helper.GenerateIndex(f'{objSerialTitle.cTitle}')}',"\
                f"s.status_at=true,"\
                f"s.updated_at='{str(datetime.now())}',"\
                f"s.created_at='{str(datetime.now())}'"\
                f"{self.__arrComman[2]}"\
                f"s.updated_at='{str(datetime.now())}'"

        cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)
        
        objIdSerial = self.__db.First(cNodeHeader)
        objSerialTitle.idSerialTitle = objIdSerial['idSerialTitle']

        return objSerialTitle
