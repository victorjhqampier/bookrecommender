from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Request.MergeBookResponseEntity import MergeBookResponseEntity
from Domain.Interfaces.IAllRelationship import IAllRelationship
from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IBook import IBook
from Domain.Interfaces.IClassification import IClassification
from Domain.Interfaces.ICopy import ICopy
from Domain.Interfaces.IItem import IItem
from Domain.Interfaces.IPublisher import IPublisher
from Domain.Interfaces.ISerialTitle import ISerialTitle
from Infrastructure.Neo4j.Nodes.AuthorNode import AuthorNode
from Infrastructure.Neo4j.Nodes.ClassificationNode import ClassificationNode
from Infrastructure.Neo4j.Nodes.CopyNode import CopyNode
from Infrastructure.Neo4j.Nodes.ItemNode import ItemNode
from Infrastructure.Neo4j.Nodes.PublisherNode import PublisherNode
from Infrastructure.Neo4j.Nodes.SerialTitleNode import SerialTitleNode
from Infrastructure.Neo4j.Relationships.RelationshipAllProgramability import RelationshipAllProgramability

class BookProgramability(IBook):    

    def __init__(self):
        self.__Item :IItem = ItemNode()
        self.__Autor : IAuthor = AuthorNode()
        self.__Publisher: IPublisher = PublisherNode()
        self.__Classification : IClassification = ClassificationNode()
        self.__Copy:ICopy = CopyNode()
        self.__SerialTitle:ISerialTitle = SerialTitleNode()
        self.__AllRelationShip:IAllRelationship = RelationshipAllProgramability()
        
    # def SaveBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
    #     pass

    # def UpdateBook (self, objItem:ItemDataEntity, arrCopies:list):
    #     pass

    def MergeBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity) -> MergeBookResponseEntity:
        
        idItem = self.__Item.GetItem(objItem)
        if idItem is not None:
            # objItem.idItem = idItem
            return MergeBookResponseEntity(
                idTitle=idItem,
                cTitle=objItem.cTitle
            ) 

        arrCopies = self.__Copy.MergeCopies(arrCopies)
        arrAuthors = self.__Autor.MergeAuthors(arrAuthors)
        arrPublisher = self.__Publisher.MergePublisher(arrPublisher)
        objClass = self.__Classification.MergeClassification(objClass)
        objSerial = self.__SerialTitle.MergeSerialTitle(objSerial)
        objItem = self.__Item.CreateItem(objItem)

        self.__AllRelationShip.MergeAllRelationships(objItem,arrCopies,arrAuthors,arrPublisher,objClass,objSerial)

        return MergeBookResponseEntity(
                idTitle=objItem.idItem,
                cTitle=objItem.cTitle
            ) 