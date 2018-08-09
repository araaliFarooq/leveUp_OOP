import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import re

def validate_email(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        return False
    # return "Very short email entered"

def validate_contact(contact):
    if len(contact) > 6:
        if re.match(r'[789]\d{9}$',contact):
            return True

        return False
    # return "Phone number has to be longer than 6 characters"    