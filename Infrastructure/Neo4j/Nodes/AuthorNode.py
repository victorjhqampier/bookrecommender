from Domain.Common.CryptographyCommon import CryptographyCommon
from Domain.Enums.CryptoEnum import CryptoEnum
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
    __crypo: ICryptography = CryptographyCommon()
    __arrComman: list = ["MERGE ", "ON CREATE SET ", " ON MATCH SET "]
    __cName: str = "Responsibles"

    def __init__(self):
        pass

    def MergeAuthors(self, arrAuthor: list):        
        nContador: int = 0
        arrQuery: list = []
        cIdentity: str = ""
        arrAlias: list = []
        arrSelect: list = []
        cNodeHeader: str = ""
        cQuery: str = ""

        for item in arrAuthor:
            arrAlias.append(f"p{str(nContador)}")
            cIdentity = self.__helper.GenerateIdentifier(f"{item.cSurname} {item.cName}")
            cNodeHeader = self.__arrComman[0] + f"(p{str(nContador)}:" + self.__cName + "{identity_at:'"+cIdentity+"'})"
            cQuery = f"{self.__arrComman[1]}"\
                f"{arrAlias[nContador]}.cSurname='{self.__helper.FormateText(item.cSurname)}',"\
                f"{arrAlias[nContador]}.cName='{self.__helper.FormateText(item.cName)}',"\
                f"{arrAlias[nContador]}.cPlace='{self.__helper.FormateText(item.cPlace.upper())}',"\
                f"{arrAlias[nContador]}.index_at='{self.__helper.GenerateIndex(f'{item.cSurname} {item.cName}')}',"\
                f"{arrAlias[nContador]}.status_at=true,"\
                f"{arrAlias[nContador]}.updated_at='{str(datetime.now())}',"\
                f"{arrAlias[nContador]}.created_at='{str(datetime.now())}'"\
                f"{self.__arrComman[2]}"\
                f"{arrAlias[nContador]}.updated_at='{str(datetime.now())}'"
            arrSelect.append(f"ID({arrAlias[nContador]})")
            nContador += 1
            arrQuery.append(f"{cNodeHeader} {cQuery}")

        cNodeHeader = " ".join(arrQuery) + self.__db.Select(f"[{','.join(arrSelect)}] AS idAuthor")
        arrList: list = self.__db.First(cNodeHeader)
        nContador = 0
        for item in arrAuthor:
            item.idAuthor = str(arrList["idAuthor"][nContador])
            nContador += 1
        return arrAuthor
