#This program is used to find the nth number in the fibonacci sequence

def main():
    n = int(input("Enter a value of n: "))
    old , new = 1, 1
    for i in range(n-2):
        new, old = old+new, new
        
    print("The nth term is: ", new)

main()
