from dataclasses import dataclass
from datetime import datetime

@dataclass
class AuthorDataEntity:
    idAuthor:str
    cName:str
    cSurname:str
    cPlace:str
    cRole:str