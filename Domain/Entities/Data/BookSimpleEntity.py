from dataclasses import dataclass
from typing import Optional

@dataclass
class BookSimpleEntity:
    idTitle:str
    cTitle:str
    cSubtitle:Optional[str]
    cTopic:Optional[str]
    cRelease:Optional[str]
    cImage:Optional[str]
    cAuthor:Optional[str]
    cRole:Optional[str]
    nViews:int

