from dataclasses import dataclass
from datetime import datetime

@dataclass
class ItemDataEntity:
    idItem:str
    cTitle:str
    cSubtitle:str
    cEdition:str
    nReleased:int
    cContent:str
    cIsbn:str
    cNotes:str
    cPhysicalDescription:str
    cTopics:str
    cType:str
    cImage:str
    cLink:str