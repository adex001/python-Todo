import os
from flask import Flask, request, jsonify
from flask_restplus import Api
from config import config
from blueprint import api_blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api(api_blueprint)

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/adeoyeolatunbosun/Documents/python-todo/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    app_context = app.app_context()
    app_context.push()


    @app.route('/')
    def HelloTodo():
        return jsonify({'data': 'Welcome to my To-Do API'})
    from views import TodoResource, TodoSingleResource

    app.register_blueprint(api_blueprint)

    db.create_all()
    return app
