from flask import Blueprint

auth = Blueprint('auth',__name__)

from .models import *
# from . import views,forms