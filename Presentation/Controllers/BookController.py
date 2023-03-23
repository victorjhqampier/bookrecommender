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

#=======================================================================
#   © Victor JCaxi - All rights reserved
#-----------------------------------------------------------------------
#   Aim         : Registrar / Mesclar un libro sobre Neo4j Database
#   Created     : 22-03-2023
#   By          : Victor JCaxi
#-----------------------------------------------------------------------
#   Changes:
#   By        Date       Aim
#=======================================================================

EasyResponse: IEasyResponse = EasyResponseCommon()
BookHandler: IBook = BookProgramability()

bookController = Blueprint("bookController", __name__)
CORS(bookController)

@bookController.route("/save-merge", methods=["POST"])
@jwt_required()
def SaveMergeBook():
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