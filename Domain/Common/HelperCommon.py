import re
from unicodedata import normalize
import hashlib
from Domain.Interfaces.IHelper import IHelper
class HelperCommon(IHelper):
    __StopWords=["a","con","de","al","e","en", "ademas","tal","sus","el","entre","sido","asi","desde","ella","ello","del","es","estas","sin","esto","han","estos","esta","este","ha","pe","com","como","he","la","las","los","les","mas","mi","me","muy","no","o","para","por","que","se","si","son","su","tu","un","una","y","ya","yo","tus","tu","te","lo"]
    
    def __init__(self):
        pass   

    def GenerateIdentifier(self, cString:str):
        cString = normalize("NFD", cString.lower())
        cString = ''.join([char for char in cString if char.isalnum() or char.isspace()])
        #cString = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", cString, 0, re.I)
        cString = ''.join([word for word in cString.split() if word not in self.__StopWords and len(word) > 2]).strip()
        arrBytes = cString.encode('utf-8')
        objHash = hashlib.sha256(arrBytes)
        return objHash.hexdigest()

    def GenerateIndex(self, cString:str):
        cString = normalize("NFD", cString.lower())
        cString = ''.join(char for char in cString if char.isalnum() or char.isspace())
        arrWords = cString.split()
        arrWords = [word for word in arrWords if word not in self.__StopWords and len(word) > 2]
        return " ".join(sorted(arrWords)).strip()

    def FormateText(self, cString:str):
        if(cString == ""):
            return ""
        return " ".join(cString.split())