from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.ICopy import ICopy
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class CopyNode(ICopy):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __cName: str = "Copies"
    __cAlias:str = "e"

    def __init__(self):
        pass

    def MergeCopies(self, arrCopies: list):   
        nContador: int = 0
        cIdentity: str = ""
        arrAlias: list = []
        arrSelect:list = []        
        arrNodeSaving = self.__db.Node()
        result:list =[]

        for item in arrCopies:
            if(item.cCode == ''):
                raise Exception("CNombre no puede estar vacio.")

            arrAlias.append(self.__cAlias + str(nContador))
            arrSelect.append(f"ID({arrAlias[nContador]})")
            cIdentity = self.__helper.GenerateIdentifier(f"{item.cCode} {item.cNotation}")

            arrNodeSaving.Merge(arrAlias[nContador],self.__cName, cIdentity
                ).OnCreate(
                    {
                        "cCode":self.__helper.FormateText(item.cCode),
                        "cNotation":self.__helper.FormateText(item.cNotation.upper()),
                        "cLibrary":self.__helper.FormateText(item.cLibrary.title()),
                        "cLink":self.__helper.FormateText(item.cLink),
                        "status_at":True,
                        "updated_at":str(datetime.now()),
                        "created_at":str(datetime.now())
                    }
                ).OnMatch(
                    {                        
                        "updated_at":str(datetime.now())
                    }
                ).Select(f"[{','.join(arrSelect)}] AS idCopy")
            nContador += 1

        result = arrNodeSaving.FirstOrDefault()
        nContador = 0
        for item in arrCopies:
            item.idCopy = str(result["idCopy"][nContador])
            nContador += 1
        return arrCopies
