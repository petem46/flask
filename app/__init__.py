from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views
from app import dashboard
from app import upload