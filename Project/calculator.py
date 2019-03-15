#McKinley Fox
#This is the graphic interface for the calculator

from calc_functions import *

def main():
    equation = input("Enter an equation (use spaces in between): ").split()
    result = getEquation(equation)
    print ("The result of the equation is", result)
   

main()
