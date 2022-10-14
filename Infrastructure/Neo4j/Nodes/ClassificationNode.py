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
    __cName: str = "Classifications"
    __cAlias:str = "r"

    def __init__(self):
        pass

    def MergeClassification(self, objClassification: ClassificationDataEntity):
                       
        cIdentity: str = ""       
        arrNodeSaving = self.__db.Node()      
        
        if(objClassification.cCode == ''):
            raise Exception("CNombre no puede estar vacio.")
        
        cIdentity = self.__helper.GenerateIdentifier(f"{objClassification.cCode}")
        arrNodeSaving.Merge(self.__cAlias,self.__cName, cIdentity
                ).OnCreate(
                    {
                        "cCode":self.__helper.FormateText(objClassification.cCode),
                        "cDescription":self.__helper.FormateText(objClassification.cDescription.title()),
                        "index_at":self.__helper.GenerateIndex(f'{objClassification.cCode} {objClassification.cDescription}'),
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                ).Select(f"ID ({self.__cAlias}) AS idClassification")
        
        result = arrNodeSaving.FirstOrDefault()
        objClassification.idClassification = result['idClassification']
        return objClassification
        # return result
        # cNodeHeader = self.__arrComman[0] + f"(c:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
        # cQuery = f"{self.__arrComman[1]}"\
        #         f"c.}',"\
        #         f"c.}',"\
        #         f"c.index_at='{}',"\
        #         f"c.status_at=true,"\
        #         f"c.updated_at='{str(datetime.now())}',"\
        #         f"c.created_at='{str(datetime.now())}'"\
        #         f"{self.__arrComman[2]}"\
        #         f"c.updated_at='{str(datetime.now())}'"

        # cNodeHeader = cNodeHeader + cQuery + self.__db.Select(self.__cReturn)
        
        # objIdClass = self.__db.First(cNodeHeader)
        # objClassification.idClassification = objIdClass['idClassification']
        # return objClassification
