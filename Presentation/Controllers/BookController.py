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
from Domain.Interfaces.IHelper import IHelper
from Domain.Common.HelperCommon import HelperCommon
from Domain.Interfaces.IRecomInfrastructure import IRecomInfrastructure
from Infrastructure.Neo4j.Programmabilities.BookProgramability import BookProgramability
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required
from Infrastructure.Neo4j.Programmabilities.RecomMethod import RecomMethod
import logging

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

Logger = logging.getLogger(__name__)#WARNING, ERROR y CRITICAL
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
Logger.addHandler(console_handler)

EasyResponse: IEasyResponse = EasyResponseCommon()
Helper: IHelper = HelperCommon()

BookHandler: IBook = BookProgramability() # No Global yet
objRecom:IRecomInfrastructure = RecomMethod()

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
        Logger.error("bookController /save-merge : [%s] WITH INPUT %s", str(e), str(request.get_json()))
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))

@bookController.route("/search", methods=["GET"])
@jwt_required()
def SearchBook():
    try:
        cKeyWord:str = request.args["cKeyWord"] 
        if(len(cKeyWord) < 4):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())
        
        cKeyWord = Helper.GenerateIndex(cKeyWord)
        if(len(cKeyWord) < 4):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())

        result:list = objRecom.SearchBook(cKeyWord)
        if(len(result) == 0):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())

        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        Logger.error("bookController /search : [%s] WITH INPUT %s", str(e), str(request.args["cKeyWord"]))
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))

@bookController.route("/trends", methods=["GET"])
@jwt_required()
def TrendsBook():
    try:
        result:list = objRecom.GetTrends()
        if(len(result) == 0):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())

        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        Logger.error("bookController /trends : [%s] WITH INPUT %s", str(e), "None")
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))

@bookController.route("/show-book", methods=["POST"])
@jwt_required()
def GetBook():
    try:
        idTitle:str = request.get_json()["idTitle"]
        
        result = BookHandler.GetBook(int(idTitle))
        # if(len(result) == 0):
        #     return StatusCode(200, EasyResponse.EasyEmptyRespond())
        objRecom.UpdateViews(int(idTitle))
        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        Logger.error("bookController /show-book : [%s] WITH INPUT %s", str(e), str(request.get_json()))
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))