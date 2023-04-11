from flask import Blueprint
from . import scheduleController


schedule_bp = Blueprint("schedule", __name__, url_prefix="/schedule")
