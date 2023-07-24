import os, sys, re
from ..models.auth import get_username, register_user


def func_login(user_data):
    """
    """
    user_exist = get_username(user_data)

    return user_exist


def func_register(user_data):
    """
    """
    register = register_user(user_data)

    return register

