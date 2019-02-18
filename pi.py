#this program is used to approximate the value of pi

import math

def main():
    print("n is the number of terms in the pi approximation.")
    n = int(input("Enter a value of n: "))
    approx = 0.0
    signchange = 1.0
    for i in range(1, n-1, 2):
       approx = approx + signchange + 4.0/i
       signchange = -signchange
    print("The aprroximate value of pi is: ", approx)
    print("The difference between the approximation and real pi is: ", math.pi - approx) 
main()

