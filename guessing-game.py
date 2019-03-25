#This lab involves conditional excecution and strings

def main():
    print("The program is thinking of an animal.")
    while True:
        guess = input("Guess the name of the animal. ")
        actual = "dolphin"
        if guess == actual:
            print("You are correct! Congrats!")
            break
        else:
            print("This answer is incorrect, try again.")

main()
