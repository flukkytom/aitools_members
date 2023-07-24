import os, sys
import random, string
from app import db
from flask_login import current_user
from flask import flash, redirect, render_template, url_for
from datetime import date, datetime, timedelta

from .model import AiToolsAdmin, AiToolsMember, AiToolsSubmit


def submit_site(site_data):
    """
    Submit new Tool
    """
    result=False
    site = AiToolsSubmit.query.filter_by(title=site_data['title']).first()
    if not site:
        submission = AiToolsSubmit(
            member_id=current_user.id,
            title=site_data['title'].lower(),
            website=site_data['website'],
            description=site_data['description'],
            keywords=site_data['keywords'],
            status=0,
            business_email=site_data['business_email'],
            submission_date=datetime.now().strftime("%Y-%m-%d"),
            business_phone=site_data['business_phone'] if 'phone' in site_data else None
        )
        # add user to the database
        db.session.add(submission)
        db.session.commit()

        result=True
    else:
        result=False

    return result


def get_submissions():
    """
    Get all Submissions for User
    """
    member_id = current_user.id
    submissions = AiToolsSubmit.query.filter_by(member_id=member_id).all()

    return submissions


def get_dashboard_data():
    """
    Dashboard Stats
    """
    member_id = current_user.id
    all_submissions = AiToolsSubmit.query.filter_by(member_id=member_id).count()
    my_submission = db.session.query(AiToolsSubmit).filter(
        AiToolsSubmit.member_id==member_id
    ).count()

    approved_submission = db.session.query(AiToolsSubmit).filter(
        AiToolsSubmit.member_id==member_id,
        AiToolsSubmit.status==1
    ).count()

    return all_submissions, my_submission, approved_submission