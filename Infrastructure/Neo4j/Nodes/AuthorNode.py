from Domain.Common.CryptographyCommon import CryptographyCommon
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Enums.NodeEnum import NodeEnum
from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.ICryptography import ICryptography
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class AuthorNode(IAuthor):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __cName: str = NodeEnum.Responsibles
    __cAlias:str = "p"

    def __init__(self):
        pass

    def MergeAuthors(self, arrAuthor: list):        
        nContador: int = 0
        cIdentity: str = ""
        arrAlias: list = []
        arrSelect:list = []        
        arrNodeSaving = self.__db.Node()
        result:list =[]

        for item in arrAuthor:
            if(item.cSurname == ''):
                raise Exception("CNombre no puede estar vacio.")

            arrAlias.append(self.__cAlias + str(nContador))
            arrSelect.append(f"ID({arrAlias[nContador]})")
            cIdentity = self.__helper.GenerateIdentifier(f"{item.cSurname} {item.cName}")

            arrNodeSaving.Merge(arrAlias[nContador],self.__cName, cIdentity
                ).OnCreate(
                    {
                        "cSurname":self.__helper.FormateText(item.cSurname.title()),
                        "cName":self.__helper.FormateText(item.cName.title()),
                        "cPlace":self.__helper.FormateText(item.cPlace.title()),
                        "index_at":self.__helper.GenerateIndex(f'{item.cSurname} {item.cName}'),
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                )#.Select(f"[{','.join(arrSelect)}] AS idAuthor")
            nContador += 1
        arrNodeSaving.Select(f"[{','.join(arrSelect)}] AS idAuthor")
        result = arrNodeSaving.FirstOrDefault()
        
        nContador = 0
        for item in arrAuthor:
            item.idAuthor = str(result["idAuthor"][nContador])
            nContador += 1
        return arrAuthor

    def GetAuthor(self, idTitle:int)->list[AuthorDataEntity]:
        BuildToGetAuthor= self.__db.Query()
        BuildToGetAuthor.Match(            
            ).Node("Title","m"
                ).LeftRelationship("HAS_RESPONSIBILITY","au"
            ).Node("Person","pe"
            ).Where(            
                ).Id("m", idTitle
            ).Select("ID(pe) AS idAuthor, pe.cName AS cName, pe.cSurname AS cSurname, pe.cPlace AS cPlace, au.cRole AS cRole")            
                
        return BuildToGetAuthor.ToList()