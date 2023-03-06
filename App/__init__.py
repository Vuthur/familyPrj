from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile("config.py")


api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 导入路由
from . import ScheduleModel
from . import UserModel
from . import FamilyModel
