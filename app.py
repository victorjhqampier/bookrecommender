from flask import Flask
from flask.json import jsonify
from flask_jwt_extended import JWTManager
from Domain.Enums.TokenEnum import TokenEnum

from Presentation.Controllers.DefaultController import defaultController
from Presentation.Controllers.PruebaController import pruebaController
from Presentation.Controllers.BookController import bookController
from Presentation.Controllers.AuthController import authenticationController
from Presentation.Controllers.RecomController import recomController

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = TokenEnum.Key
jwt = JWTManager(app)

app.register_blueprint(defaultController)
app.register_blueprint(authenticationController, url_prefix="/api/recommendations/1.0/authentication")
app.register_blueprint(bookController,url_prefix="/api/recommendations/1.0/books")
app.register_blueprint(recomController,url_prefix="/api/recommendations/1.0/books/recom")
app.register_blueprint(pruebaController)

def axpag_no_found(error):
    response = jsonify({'code':404})
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.register_error_handler(404,axpag_no_found)
    app.run(debug=True,port='5007',host='0.0.0.0')

#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
#How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 18.04