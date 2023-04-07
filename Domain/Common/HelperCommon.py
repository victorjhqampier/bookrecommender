import re
from unicodedata import normalize
from Domain.Interfaces.IHelper import IHelper
class HelperCommon(IHelper):
    __StopWords=["a","con","de","al","e","en", "ademas","tal","sus","el","entre","sido","asi","desde","ella","ello","del","es","estas","sin","esto","han","estos","esta","este","ha","pe","com","como","he","la","las","los","les","mas","mi","me","muy","no","o","para","por","que","se","si","son","su","tu","un","una","y","ya","yo","tus","tu","te","lo"]
    
    def __init__(self):
        pass   

    def GenerateIdentifier(self, cString:str):
        cString = re.sub( r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize( "NFD", cString.lower()), 0, re.I)
        arrTemp = [x for x in cString.split(" ") if x not in self.__StopWords and len(x) > 2]
        cString = ''.join([char for char in " ".join(arrTemp) if char.isalnum()])
        return cString

    def GenerateIndex(self, cString:str):
        cString = re.sub( r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize( "NFD", cString.lower()), 0, re.I)
        arrTemp = sorted([''.join(char for char in x if char.isalnum()) for x in cString.split(" ") if x not in self.__StopWords and len(x) > 2])
        cString = " ".join(arrTemp).strip()
        return cString

    def FormateText(self, cString:str):
        if(cString == ""):
            return ""
        return " ".join(cString.split())