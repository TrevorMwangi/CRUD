# app/about/__init__.py

from flask import Blueprint, render_template

about = Blueprint('about', __name__)

from . import views
