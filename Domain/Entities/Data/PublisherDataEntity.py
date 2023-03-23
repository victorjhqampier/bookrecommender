from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class PublisherDataEntity:
    idPublisher:Optional[str]
    cName:str
    cPlace:Optional[str]