from Models import Users

users =[]

class SignUp(object):
    def __init__(self, first_name, second_name, contact, email):
        self.first_name = first_name
        self.second_name = second_name
        self.contact = contact
        self.email = email

    def combine_names(self, first_name, second_name):
        full_name = first_name +" "+ second_name
        return full_name

    def submit(self, first_name, second_name, contact, email):
        pass

    def validate_data(self):
              