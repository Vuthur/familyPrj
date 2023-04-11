from flask import Blueprint
from . import userController


user_bp = Blueprint("user", __name__, url_prefix="/user")
