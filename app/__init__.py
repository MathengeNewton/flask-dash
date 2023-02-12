# -*- encoding: utf-8 -*-

import os

# import Flask 
from flask import Flask, request, redirect, url_for
from .models import Users
import os
from .extensions import (
    db,
    login_manager,
)

from .config import Config


# create app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
# initialize the app with the extension
db.init_app(app)

# load Configuration
app.config.from_object( Config ) 

login_manager.init_app(app)

# Flask Login Management
@login_manager.user_loader
def load_user(user_id):
    # Replace this with your own logic to fetch the user object
    return Users.fetch_by_id(user_id)

@app.before_request
def redirect_unauthenticated():
    current_user = True
    
    if not current_user and request.endpoint != "login":
        return redirect(url_for("login"))

# Import routing to render the pages
from app import views

