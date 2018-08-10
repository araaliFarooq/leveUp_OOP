from Models import Users
from validation import validate_contact, validate_email


all_users =[]

def combine_names(first_name, second_name):
    full_name = first_name +" "+ second_name
    return full_name

# def show_all_users():
#     if len(users) > 0:
#         print( user.__dict__ for user in users)

    # print("No users added yet")    

def submit():
    first_name = input("Enter your first name: ")
    second_name = input("Enter your last name: ")
     
    while True:
        contact = input("Enter your phone number [format : xxx-xxxxxxx]: ")
        if validate_contact(contact) == False:
            print("Wrong phone number entered")
            continue
        else:
            break   
        
    while True:
        email = input("Enter your email address [format : xxxxx@x.x] : ")
        if validate_email(email) == False:
            print("Wrong email address entered")
            continue
        else:
            break    

    full_name = combine_names(first_name, second_name)

    new_user = Users(full_name, contact, email)
    all_users.append(new_user)

    print("New user added:")

    for user in all_users:
        print( "full name: "+user.full_name )
        print( "Contact: "+user.contact )
        print( "Email: "+user.email )

if __name__ == '__main__':
    submit()    
        
     

   
              