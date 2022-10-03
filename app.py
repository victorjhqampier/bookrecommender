from flask import Flask
from flask.json import jsonify
from flask_jwt_extended import JWTManager
from Domain.Enums.TokenEnum import TokenEnum

from Presentation.Controllers.DefaultController import defaultController
from Presentation.Controllers.PruebaController import pruebaController

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = TokenEnum.Key
jwt = JWTManager(app)

app.register_blueprint(defaultController)
app.register_blueprint(pruebaController)

def axpag_no_found(error):
    response = jsonify({'code':404})
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.register_error_handler(404,axpag_no_found)
    app.run(debug=True,port='5007',host='0.0.0.0')