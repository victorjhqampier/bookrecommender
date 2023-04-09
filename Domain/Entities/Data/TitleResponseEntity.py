from dataclasses import dataclass
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.CopyDataEntity import CopyDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity

@dataclass
class TitleResponseEntity:   
    title:ItemDataEntity
    classification:ClassificationDataEntity
    person:list[AuthorDataEntity]
    publisher:list[PublisherDataEntity]
    serialTitle:SerialTitlesDataEntity
    copy:list[CopyDataEntity]
