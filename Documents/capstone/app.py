from flask import Flask;
from dotenv import load_dotenv;
from firestore import add_data
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  
API_URL = "/swagger/v1.json"   

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)

@app.route("/")
def index_page():
  add_data("auth","id",{ "name": "Bayu", "email": "bayu@gmail.com", "token": "asjdfk" })
  return "hallo"