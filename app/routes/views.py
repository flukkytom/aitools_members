import os, sys
from . import aitools_app
from flask import flash, render_template, redirect, url_for, request, make_response, session
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from ..functions.auth import func_login, func_register
from ..functions.views import func_submission, func_get_submission, func_dashboard


@aitools_app.route('/', methods=['GET', 'POST'])
def login():
    """
    Login Page
    """
    if request.method == "POST":
        user_data = request.form.to_dict() 
        user_exist = func_login(user_data)

        print(user_exist);

        if user_exist:
            return redirect(url_for('.dashboard', stk=1200))

    response = make_response( 
        render_template(
            "login.html"
        )
    )       
    return response  


@aitools_app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Login Page
    """
    if request.method == "POST":
        user_data = request.form.to_dict() 
        register_user = func_register(user_data)
    
        if register_user:
            return redirect(url_for('.login', stk=1200))

    response = make_response( 
        render_template(
            "register.html"
        )
    )       
    return response  


@aitools_app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def dashboard():
    """
    Registration Page
    """
    submission = func_get_submission()
    all_submissions, my_submission, approved_submission, not_approved = func_dashboard()
    return render_template(
        "dashboard.html",
        submission=submission,
        all_submissions=all_submissions,
        my_submission=my_submission,
        approved_submission=approved_submission,
        not_approved=not_approved
    )


###Logout###############################################################
@aitools_app.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an customer out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('.login'))


###Submission###############################################################
@aitools_app.route('/submit', methods=['GET', 'POST'])
@login_required
def submission():
    """
    Submit New AI Tool
    """
    info = ""
    if request.method == "POST":
        site_data = request.form.to_dict() 
        print(site_data)
        submit_url = func_submission(site_data)
    
        if submit_url:
            return redirect(url_for('.dashboard', stk=2300))
        else:
            info = "There is error with the submission"

    return render_template(
        "submission.html",
        info=info
    )


###Help###############################################################
@aitools_app.route('/help')
@login_required
def help():
    """
    Help Page
    """
    return render_template(
        "help.html"
    )