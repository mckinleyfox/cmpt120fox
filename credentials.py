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

def password(passwd):
    if len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        print("Make sure your password is at least 8 letters")
        passwd = input("Create a new password: ")
    if passwd.upper() == passwd:
        print("Fool of a Took! That password is feeble!")
        print("Make sure your password is at least 8 letters")
        passwd = input("Create a new password: ")
    if passwd.lower() == passwd:
        print("Fool of a Took! That password is feeble!")
        print("Make sure your password is at least 8 letters")
        passwd = input("Create a new password: ")
    else:
        print("The force is strong in this one...")
    # Return?

def getPasswordStrength(passwd):
    passwd = input("Create a new password: ")
    getPassword(passwd)

    print("Your password is: ", passwd)
    print("Account configured. Your new email address is", user.lower() + "@marist.edu")

    

def main():
    name= getName()
    user = uname(name)
    passwd = password()
    passwordstrength = getPasswordStrength(passwd)
    
main()
