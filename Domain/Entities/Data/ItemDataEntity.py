from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ItemDataEntity:
    idTitle:Optional[str]
    cTitle:str
    cSubtitle:str
    cEdition:str
    nReleased:int
    cContent:str
    cIsbn:str
    cNotes:str
    # cPhysicalDescription:Optional[str]
    cTopics:str
    cType:str
    cImage:str
    dUpdated:Optional[datetime]
    # cLink:Optional[str]