# from .blueprint import apiv1
from allinone.config.default_config import Config
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os 
from flask_swagger_ui import get_swaggerui_blueprint

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')
app = Flask(__name__, static_url_path='', template_folder=TEMPLATE_PATH)
app.secret_key = 'development'
app.config.from_object(Config)
from flask_restx import Api, Resource, reqparse

db = SQLAlchemy(app)
mail = Mail(app)
from flask import Blueprint
from flask_restx import Api, Resource, reqparse
from allinone.restful.v1 import agent
from flask_restx import Resource, Namespace 

ns = Namespace(name='db', description='MSSQL db agents related apis')
ns.add_resource(agent.AgentHistoryShow, '/') 

api = Api(title='Restx APIs',version='1.0',description='Flask Restx Apis Example')
api.add_namespace(ns)
api.init_app(app)

@app.route('/')
def index(): 
    return render_template("test.html")

@app.route('/blueprints')
def get_bp_urls(): 
    return [str(p) for p in app.url_map.iter_rules()]