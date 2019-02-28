# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
     # Created: YYYY-MM-DD
def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return[first, last]

def uname(name):
    return name[0] + "." + name[1]

def password():
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8 character
    while (len(passwd)<8):
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    return passwd
        
def main():
    # get user's first and last name
    name= getName()
    user = uname(name)
    passwd = password()
    # TODO modify this to generate a Marist-style username
    # ask user to create a new password
    
    print("Account configured. Your new email address is", user + "@marist.edu")
main()
