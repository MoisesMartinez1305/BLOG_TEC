from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Importing models
from app.models import Post

##Importar blueprints
from app.routes.post import posts_bp

with app.app_context():
    db.create_all()

app.register_blueprint(posts_bp, url_prefix='/posts')

@app.route('/')
def index():
    return "Hello, World!"
