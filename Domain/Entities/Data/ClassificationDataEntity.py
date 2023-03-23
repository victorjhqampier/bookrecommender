from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ClassificationDataEntity:
    idClassification:Optional[str]
    cCode:str
    cDescription:Optional[str]