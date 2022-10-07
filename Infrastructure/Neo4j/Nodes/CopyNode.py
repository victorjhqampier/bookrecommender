from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.ICopy import ICopy
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Infrastructure.Neo4j.DbContext import DbContext
from datetime import datetime

class CopyNode(ICopy):

    __db: IContext = DbContext()
    __helper: IHelper = HelperCommon()
    __arrComman: list = ["MERGE ", "ON CREATE SET ", " ON MATCH SET "]
    __cName: str = "Copies"

    def __init__(self):
        pass

    def MergeCopies(self, arrCopies: list):   
        nContador: int = 0
        arrQuery: list = []
        cIdentity: str = ""
        arrAlias: list = []
        arrSelect: list = []
        cNodeHeader: str = ""
        cQuery: str = ""

        for item in arrCopies:
            arrAlias.append(f"e{str(nContador)}")
            cIdentity = self.__helper.GenerateIdentifier(f"{item.cCode} {item.cNotation}")
            cNodeHeader = self.__arrComman[0] + f"(e{str(nContador)}:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
            cQuery = f"{self.__arrComman[1]}"\
                f"{arrAlias[nContador]}.cCode='{self.__helper.FormateText(item.cCode)}',"\
                f"{arrAlias[nContador]}.cNotation='{self.__helper.FormateText(item.cNotation)}',"\
                f"{arrAlias[nContador]}.cLibrary='{self.__helper.FormateText(item.cLibrary.upper())}',"\
                f"{arrAlias[nContador]}.cLink='{self.__helper.FormateText(item.cLink)}',"\
                f"{arrAlias[nContador]}.status_at=true,"\
                f"{arrAlias[nContador]}.updated_at='{str(datetime.now())}',"\
                f"{arrAlias[nContador]}.created_at='{str(datetime.now())}'"\
                f"{self.__arrComman[2]}"\
                f"{arrAlias[nContador]}.updated_at='{str(datetime.now())}'"
            arrSelect.append(f"ID({arrAlias[nContador]})")
            nContador += 1
            arrQuery.append(f"{cNodeHeader} {cQuery}")

        cNodeHeader = " ".join(arrQuery) + self.__db.Select(f"[{','.join(arrSelect)}] AS idCopy")

        arrList: list = self.__db.First(cNodeHeader)
        nContador = 0
        for item in arrCopies:
            item.idCopy = str(arrList["idCopy"][nContador])
            nContador += 1
        return arrCopies
