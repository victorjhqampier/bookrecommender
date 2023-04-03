from flask import Blueprint,request
from Domain.Core.StatusCode import StatusCode,FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.CopyDataEntity import CopyDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Response import Response
from datetime import datetime

from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IBook import IBook
from Domain.Interfaces.IClassification import IClassification
from Domain.Interfaces.ICopy import ICopy
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Interfaces.IItem import IItem
from Domain.Interfaces.IPublisher import IPublisher
from Domain.Interfaces.ISerialTitle import ISerialTitle
from Infrastructure.Neo4j.Nodes.AuthorNode import AuthorNode
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Infrastructure.Neo4j.Nodes.ClassificationNode import ClassificationNode
from Infrastructure.Neo4j.Nodes.CopyNode import CopyNode
from Infrastructure.Neo4j.Nodes.ItemNode import ItemNode
from Infrastructure.Neo4j.Nodes.PublisherNode import PublisherNode
from Infrastructure.Neo4j.Nodes.SerialTitleNode import SerialTitleNode
from Infrastructure.Neo4j.Programmabilities.BookProgramability import BookProgramability
from Infrastructure.Neo4j.Programmabilities.TestMethod import TestMethod

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
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))
