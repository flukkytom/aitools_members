
import os, sys
import random, string
from app import db
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from .model import AiToolsAdmin, AiToolsMember
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta



def get_username(user_data):
    """
    """
    # check whether Customer exists in the database and whether
    # the password entered matches the password in the database
    result = False
    user = AiToolsMember.query.filter_by(email=user_data['email']).first()
    
    if user is not None:
        passwd_check = check_password_hash(user.password, user_data['password'])
        print(user, user.password, user_data['password'],passwd_check, generate_password_hash(user_data['password']))
        if passwd_check:
            # log customer in
            login_user(user)
            result = True
        else:
            result = False

    # when login details are incorrect
    else:
        result = False

    return result


def register_user(user_data):
    """
    """
    result=False
    user = AiToolsMember.query.filter_by(email=user_data['email']).first()
    if not user:
        member = AiToolsMember(
            email=user_data['email'].lower(),
            password=generate_password_hash(user_data['password']),
            country=user_data['country'],
            firstname=user_data['firstname'],
            lastname=user_data['lastname'],
            last_login=datetime.now().strftime("%Y-%m-%d"),
            phone=user_data['phone'] if 'phone' in user_data else None
        )
        # add user to the database
        db.session.add(member)
        db.session.commit()

        result=True
    else:
        result=False

    return result
