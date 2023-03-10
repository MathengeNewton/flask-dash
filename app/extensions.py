from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_required


login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()