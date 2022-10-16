from Domain.Interfaces.IAutenticacion import IAutenticacion

class AutenticacionDatabase(IAutenticacion):
    __users = [
        {"user_id":1,"user":"admin","paswd":"1234567++","status":True},
        {"user_id":2,"user":"admin1","paswd":"todos me llegan a ña punta","status":True},
        {"user_id":3,"user":"admin2","paswd":"amazonas1234++","status":True}
    ]
    def __init__(self):
        pass
    def IniciarSesion(self,user:str,paswd:str):        
        try:
            data = next(x for x in self.__users if x["user"] == user and x["paswd"] == paswd and x["status"] == True)
            return data["user_id"]
        except Exception:
            return 0
        
    def VerificarIdUsuario(self,idUsuario:int):        
        try:
            next(x for x in self.__users if x["user_id"] == idUsuario and x["status"] == True)
            return True
        except Exception as ex:
            return False