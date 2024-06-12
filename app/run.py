from app.database import db
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from app.controllers.taxi_controler import taxi_bp
from app.controllers.user_controler import user_bp
from flask_jwt_extended import JWTManager

app=Flask(__name__)

app.config["JWT_SECRET_KEY"]="tu clave secreta"
SWAGGER_URL="/api/docs"
API_URL="/static/swagger.json"

swagger_ui_blueprint=get_swaggerui_blueprint(SWAGGER_URL,API_URL,config={"app_name":"OBRAJES LTDA"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///tax.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db.init_app(app)
jwt=JWTManager(app)

app.register_blueprint(taxi_bp,url_prefix="/api")
app.register_blueprint(user_bp,url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)
    

