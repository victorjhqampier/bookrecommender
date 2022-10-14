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

# Autor : IAuthor = AuthorNode()
# Publisher: IPublisher = PublisherNode()
# Classification : IClassification = ClassificationNode()
# SerialTitle:ISerialTitle = SerialTitleNode()
Item :IItem = ItemNode()
# Copy:ICopy = CopyNode()
EasyResponse:IEasyResponse = EasyResponseCommon()

pruebaController = Blueprint("pruebaController",__name__)

@pruebaController.route("/prueba",methods=["POST"])
def PruebaController():

    arrInput:list = request.get_json()
    # arrAuthorIn:list =[]
    # for item in arrInput["publishers"]:
    #     item["idPublisher"] = ''        
    #     InputEmperesa:PublisherDataEntity = FromBody(item, PublisherDataEntity)
    #     arrAuthorIn.append(InputEmperesa)
    # arrGuardarEmpre:list = Publisher.MergePublisher(arrAuthorIn)

    # arrAuthorIn:list =[]
    # for item in arrInput["responsibles"]:
    #     item["idAuthor"] = ''     
    #     InputEmperesa:AuthorDataEntity = FromBody(item, AuthorDataEntity)
    #     arrAuthorIn.append(InputEmperesa)
    # arrGuardarEmpre:list = Autor.MergeAuthors(arrAuthorIn)
    
    # arrInput['classification']['idClassification'] = ''
    # InputEmperesa:ClassificationDataEntity = FromBody(arrInput['classification'], ClassificationDataEntity)
    # intem = Classification.MergeClassification(InputEmperesa)

    # arrInput['serialTitle']['idSerialTitle'] = ''
    # InputEmperesa:SerialTitlesDataEntity = FromBody(arrInput['serialTitle'], SerialTitlesDataEntity)
    # temp = SerialTitle.MergeSerialTitle(InputEmperesa)

    arrInput['item']['idItem'] = ''
    InputEmperesa:ItemDataEntity = FromBody(arrInput['item'], ItemDataEntity)
    temp = Item.CreateItem(InputEmperesa)
    
    # arrAuthorIn:list =[]
    # for item in arrInput["copies"]:
    #     item["idCopy"] = ''        
    #     InputEmperesa:CopyDataEntity = FromBody(item, CopyDataEntity)
    #     arrAuthorIn.append(InputEmperesa)
    # arrGuardarEmpre = Copy.MergeCopies(arrAuthorIn)
    return StatusCode(200,EasyResponse.EasySuccessRespond(temp)) 
