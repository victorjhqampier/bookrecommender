from enum import Enum
class Neo4jEnum(str, Enum):
    DbPrefix="bolt"
    DbHost = "192.168.0.107"    
    DbPort="7687"
    DbName = "neo4j"
    DbUser="neo4j"
    DbPass="getthereveryfast14"