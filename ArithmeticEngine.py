# CMPT 120 - Lab #6
# McKinley Fox
# 04-1-2019
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower() 
        if cmd in ["add", "sub", "mult", "div"]:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))   
            except:
                print("Error: input is not valid")
                continue
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            if num2 == "0":
                raise Exception("Unable to divide by 0")
            else:
                result = num1 // num2
        elif cmd == "quit":
            break
        else:
            print(cmd, "is not a valid command")
            break
        print("The result is " + str(result) + ".\n") 
        
def main():
    showIntro()
    try:
        doLoop()
    except:
        print("Division by 0")
    showOutro()
    
main()
