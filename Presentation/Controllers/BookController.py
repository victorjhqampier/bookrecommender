from flask import Blueprint, request
from Domain.Core.StatusCode import StatusCode, FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.CopyDataEntity import CopyDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Interfaces.IBook import IBook
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Infrastructure.Neo4j.Programmabilities.BookProgramability import BookProgramability
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required

EasyResponse: IEasyResponse = EasyResponseCommon()

BookHandler: IBook = BookProgramability()

bookController = Blueprint("bookController", __name__)
CORS(bookController)

@bookController.route("/save", methods=["POST"])
@jwt_required()
def SaveBook():
    try:
        arrInput: list = request.get_json()

        arrPublisher: list = []
        for item in arrInput["publishers"]:
            item["idPublisher"] = ''
            Input: PublisherDataEntity = FromBody(item, PublisherDataEntity)
            arrPublisher.append(Input)

        arrAuthors: list = []
        for item in arrInput["responsibles"]:
            item["idAuthor"] = ''
            Input: AuthorDataEntity = FromBody(item, AuthorDataEntity)
            arrAuthors.append(Input)

        arrInput['classification']['idClassification'] = ''
        objclassification: ClassificationDataEntity = FromBody(
            arrInput['classification'], ClassificationDataEntity)

        arrInput['serialTitle']['idSerialTitle'] = ''
        arrInput['serialTitle']['cNumber'] = '' if arrInput['serialTitle']['cNumber'] is None else arrInput['serialTitle']['cNumber']
        arrInput['serialTitle']['cTitle'] = '' if arrInput['serialTitle']['cTitle'] is None else arrInput['serialTitle']['cTitle']
        objSerialTitle: SerialTitlesDataEntity = FromBody(
            arrInput['serialTitle'], SerialTitlesDataEntity)

        arrInput['item']['idItem'] = ''
        objItem: ItemDataEntity = FromBody(arrInput['item'], ItemDataEntity)

        arrCopies: list = []
        for item in arrInput["copies"]:
            item["idCopy"] = ''
            Input: CopyDataEntity = FromBody(item, CopyDataEntity)
            arrCopies.append(Input)

        result = BookHandler.MergeBook(
            objItem, arrCopies, arrAuthors, arrPublisher, objclassification, objSerialTitle)

        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        return StatusCode(200, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))