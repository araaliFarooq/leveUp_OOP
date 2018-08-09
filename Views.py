from Models import Users
from validation import validate_contact, validate_email


users =[]

def combine_names(first_name, second_name):
    full_name = first_name +" "+ second_name
    return full_name

def submit():
    first_name = input("Enter your first name: ")
    second_name = input("Enter your last name: ")
    contact = input("Enter your phone number: ")
    
    if not validate_contact(contact):
        print("Wrong phone number entered")

    email = input("Enter your email address: ")

    if not validate_email(email):
        print("Wrong email address entered")

    full_name = combine_names(first_name, second_name)

    new_user = Users(first_name, second_name, contact, email)       
        
     

   
              