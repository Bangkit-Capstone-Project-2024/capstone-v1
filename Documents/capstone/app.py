from flask import Flask;
from dotenv import load_dotenv;
from firestore import add_data

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index_page():
  add_data("auth","id",{ "name": "Bayu", "email": "bayu@gmail.com", "token": "asjdfk" })
  return "hallo"