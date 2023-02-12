import uuid
from app.extensions import db
from sqlalchemy_utils import UUIDType
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(45), nullable=True, unique=True)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(200),unique=False,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # this is is a static method
    def create(self):
        db.session.add(self)
        db.session.commit()

    # check if dpt exist
    @classmethod
    def check_user_exist(cls,email):
        record = cls.query.filter_by(email=email)
        if record.first():
            return True
        else:
            return False

    # fetch all users
    @classmethod
    def fetch_all_users(cls):
        return cls.query.all()

    # fetch user by id
    @classmethod
    def fetch_by_id(cls,dpt_id):
        return cls.query.filter_by(id=dpt_id).first()