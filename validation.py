import re

def validate_email(email):
    if len(email) > 7:
        if re.match("[^@]+@[^@]+\.[^@]+", email) != None:
            return True
        return False
    return False    
    

def validate_contact(contact):
    if len(contact) > 6:
        if re.match("^\d{3}-\d{7}$",contact):
            return True

        return False
    return False
       