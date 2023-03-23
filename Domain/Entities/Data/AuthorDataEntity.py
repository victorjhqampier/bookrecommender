from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class AuthorDataEntity:
    idAuthor:Optional[str]
    cName:Optional[str]
    cSurname:str
    cPlace:Optional[str]
    cRole:str