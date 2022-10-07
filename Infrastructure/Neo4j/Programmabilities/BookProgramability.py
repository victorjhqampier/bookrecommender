from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Interfaces.IAuthor import IAuthor
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


class BookProgramability():
    __Item :IItem = ItemNode()
    __Autor : IAuthor = AuthorNode()
    __Publisher: IPublisher = PublisherNode()
    __Classification : IClassification = ClassificationNode()
    __Copy:ICopy = CopyNode()
    __SerialTitle:ISerialTitle = SerialTitleNode()

    def __init__(self):
        pass
    
    def SaveBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        pass

    def UpdateBook (self, objItem:ItemDataEntity, arrCopies:list):
        pass

    def MergeBook(objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        pass
