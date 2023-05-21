from flask import Blueprint,request
from Domain.Core.StatusCode import StatusCode,FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.CopyDataEntity import CopyDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Interfaces.IBook import IBook
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Infrastructure.Neo4j.Programmabilities.TestMethod import TestMethod
import logging

Logger = logging.getLogger(__name__)#WARNING, ERROR y CRITICAL
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
Logger.addHandler(console_handler)

EasyResponse: IEasyResponse = EasyResponseCommon()
BookHandler: IBook = TestMethod()
EasyResponse:IEasyResponse = EasyResponseCommon()

pruebaController = Blueprint("pruebaController",__name__)

@pruebaController.route("/prueba",methods=["POST"])
def PruebaController():
    try:
        arrInput: list = request.get_json()

        arrPublisher: list = []
        for item in arrInput["publisher"]:
            Input: PublisherDataEntity = FromBody(item, PublisherDataEntity)
            arrPublisher.append(Input)

        arrAuthors: list = []
        for item in arrInput["person"]:
            Input: AuthorDataEntity = FromBody(item, AuthorDataEntity)
            arrAuthors.append(Input)

        objclassification: ClassificationDataEntity = FromBody(arrInput['classification'], ClassificationDataEntity)

        arrInput['serialTitle']['cTitle'] = '' if len(arrInput['serialTitle']) == 0 else arrInput['serialTitle']['cTitle']
        objSerialTitle: SerialTitlesDataEntity = FromBody(arrInput['serialTitle'], SerialTitlesDataEntity)      

        objItem: ItemDataEntity = FromBody(arrInput['title'], ItemDataEntity)

        arrCopies: list = []
        for item in arrInput["copy"]:
            Input: CopyDataEntity = FromBody(item, CopyDataEntity)
            arrCopies.append(Input)

        result = BookHandler.MergeBook(objItem, arrCopies, arrAuthors, arrPublisher, objclassification, objSerialTitle)

        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        Logger.error("pruebaController /prueba : [%s] WITH INPUT %s", str(e), str(request.get_json()))
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))
