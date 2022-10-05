from dataclasses import dataclass
from datetime import datetime

@dataclass
class PublisherDataEntity:
    idPublisher:str
    cName:str
    cPlace:str