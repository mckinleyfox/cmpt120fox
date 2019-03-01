# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: McKinley Fox
     # Created: 2019-02-25
def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return[first, last]

def uname(name):
    return name[0] + "." + name[1]

def password():
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8 character
    #while (len(passwd)<8):
        #print("Fool of a Took! That password is feeble!")
        #passwd = input("Create a new password: ")
    #print("The force is strong in this one...")
    weak = "weak"
    med = "medium"
    strong = "strong"
    if len(passwd) > 8:
        print ("password is", strong)
    elif len(passwd) < 8:
        print("password is", weak)
        passwd = input("Create a new password: ")
    if passwd.lower()== passwd or passwd.upper()==passwd:
        print ('password is', weak)
        passwd = input("Create a new password: ")
    elif passwd.lower()== passwd and passwd.upper()==passwd:
        print ('password is', med)
    else:
        passwd.lower()== passwd and passwd.upper()==passwd
        print ('password is', strong)
    return passwd

    

def main():
    # get user's first and last name
    name= getName()
    user = uname(name)
    passwd = password()
    # TODO modify this to generate a Marist-style username
    # ask user to create a new password
    
    print("Account configured. Your new email address is", user.lower() + "@marist.edu")
main()
