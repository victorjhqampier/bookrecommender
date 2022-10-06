from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Interfaces.IClassification import IClassification
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class ClassificationNode(IClassification):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __arrComman: list = ["MERGE ", " ON CREATE SET ", " ON MATCH SET "]
    __cName: str = "Classifications"
    __cReturn: str = "ID (c) AS idClassification"

    def __init__(self):
        pass

    def MergeClassification(self, objClassification: ClassificationDataEntity):
               
        cIdentity: str = ""
        cNodeHeader: str = ""
        cQuery: str = ""        
        
        if(objClassification.cCode == ''):
            raise Exception("CNombre no puede estar vacio.")
        
        cIdentity = self.__helper.GenerateIdentifier(f"{objClassification.cCode}")
        cNodeHeader = self.__arrComman[0] + f"(c:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
        cQuery = f"{self.__arrComman[1]}"\
                f"c.cCode='{self.__helper.FormateText(objClassification.cCode)}',"\
                f"c.cDescription='{self.__helper.FormateText(objClassification.cDescription)}',"\
                f"c.index_at='{self.__helper.GenerateIndex(f'{objClassification.cCode} {objClassification.cDescription}')}',"\
                f"c.status_at=true,"\
                f"c.updated_at='{str(datetime.now())}',"\
                f"c.created_at='{str(datetime.now())}'"\
                f"{self.__arrComman[2]}"\
                f"c.updated_at='{str(datetime.now())}'"

        cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)
        
        objIdClass = self.__db.First(cNodeHeader)
        objClassification.idClassification = objIdClass['idClassification']
        return objClassification
