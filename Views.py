from Models import Users
from validation import validate_contact, validate_email


all_users =[]

def combine_names(first_name, second_name):
    full_name = first_name +" "+ second_name
    return full_name

def add_new_user(full_name,contact, email):
    new_user = Users(full_name, contact, email)
    return all_users.append(new_user)
    
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
    add_new_user(full_name, contact, email)

    if len(all_users) > 0:
        print("")
        print("New user added:")
        print("--------------")

        for user in all_users:
            print("")
            print( "full name: "+user.full_name )
            print( "Contact: "+user.contact )
            print( "Email: "+user.email )

        return True
    return False    

if __name__ == '__main__':
    submit()    
        
     

   
              