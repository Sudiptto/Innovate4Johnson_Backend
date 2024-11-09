# File Description: Utility functions for the auth routes.
from .models import *
import re



# function to check if an email is a valid email
def is_valid_email(email):
    # Define a regex pattern for validating an email
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    # Check if the email matches the regex pattern
    if not re.match(email_regex, email):
        return False

    return True

# check email is in database (FOR CANIDATE )
def is_email_in_canidate(email):
    if Canidate.query.filter_by(email=email).first():
        return True
    return False

# check username is in database
def is_username_in_canidate(username):
    if Canidate.query.filter_by(username=username).first():
        return True
    return False

# check email is in database (FOR RECRUITER)
def is_email_in_recruiter(email):
    if Recruiter.query.filter_by(email=email).first():
        return True
    return False

# check if the email is a valid johnson and johnson email
def is_valid_jnj_email(email):
    # check if it's a valid johnson & johnson email -> only johnson & johnson recruiters can sign up
    if email.endswith('@jnj.com') or email.endswith('@its.jnj.com'):
        return True
    return False



#