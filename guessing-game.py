#This lab involves conditional excecution and strings

def main():
    actual = "dolphin"
    while True:
        print("The program is thinking of an animal.")
        guess = input("Guess the name of the animal. ").lower()
        if guess == actual:
            print("You are correct! Congrats!")
            break
        elif guess == "quit":
            print("Game over")
            break
        else:
            print("This answer is incorrect, try again.")
main()
