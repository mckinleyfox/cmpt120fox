#This lab involves conditional excecution and strings

def main():
    actual = "dolphin"
    while True:
        print("The program is thinking of an animal.")
        guess = input("Guess the name of the animal. ").lower()
        if guess[0] == "q" :
            print("Game over")
            break
        elif guess == actual:
            print("You are correct! Congrats!")
            like = input("Do you like dolphins?(y=yes and n=no)")
            if like == "y":
                print("Yay! That is awesome!")
            elif like == "n":
                print("Aw man! It's my favorite animal!")
            break
        else:
            print("This answer is incorrect, try again.")
main()
