from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Enums.NodeEnum import NodeEnum
from Domain.Interfaces.IClassification import IClassification
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class ClassificationNode(IClassification):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __cName: str = NodeEnum.Classification
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

    def GetClassification(self, idTitle:int)->ClassificationDataEntity:
        BuildToGetTitle= self.__db.Query()
        BuildToGetTitle.Match(            
            ).Node("Title","m"
                ).LeftRelationship("ASSIGN_DEWEY"
            ).Node("Classification","cla"
            ).Where(            
                ).Id("m", idTitle
            ).Select("ID(cla) AS idClassification, cla.cCode AS cCode, cla.cDescription AS cDescription")
                
        return BuildToGetTitle.FirstOrDefault()