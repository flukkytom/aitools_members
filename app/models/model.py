from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class AiToolsMember(UserMixin, db.Model):
    """
    Member Table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'member_access'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, unique=True)
    lastname = db.Column(db.String(128))
    country = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(255))
    last_login = db.Column(db.String(64))


class AiToolsAdmin(UserMixin, db.Model):
    """
    Customer table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'admin_access'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer)
    password = db.Column(db.String(64))
    login_status = db.Column(db.String(64))
    date_added = db.Column(db.String(64))


class AiToolsSubmit(UserMixin, db.Model):
    """
    Customer table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'submissions'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    title = db.Column(db.String(64))
    website = db.Column(db.String(64))
    description = db.Column(db.String(64))
    keywords = db.Column(db.String(64))
    business_email = db.Column(db.String(64))
    business_phone = db.Column(db.String(64))
    submission_date = db.Column(db.String(64))
    sub_data = db.Column(db.String(64))
    status = db.Column(db.String(64))