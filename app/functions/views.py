import os, sys, re, json

from ..models.views import submit_site, get_submissions, get_dashboard_data


def func_submission(site_data):
    """
    """
    save_site = submit_site(site_data)

    return save_site


def func_get_submission():
    """
    """
    get_submission = get_submissions()

    return get_submission


def func_dashboard():
    """
    """
    all_submissions, my_submission, approved_submission = get_dashboard_data()
    
    not_approved = my_submission - approved_submission

    return all_submissions, my_submission, approved_submission, not_approved


