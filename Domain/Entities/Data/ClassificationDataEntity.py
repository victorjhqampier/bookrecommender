from dataclasses import dataclass
from datetime import datetime

@dataclass
class ClassificationDataEntity:
    idClassification:str
    cCode:str
    cDescription:str