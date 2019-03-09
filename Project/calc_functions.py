#this program generates a calculator
#McKinley Fox
#Project 1
#2019-02-25

#This creates the formulas
def multiply(num1, num2):
    return float(num1) * float(num2)
   
def divide(num1, num2):
    return float(num1) / float(num2)
   
def add(num1, num2):
    return float(num1) + float(num2)

def subtract(num1, num2):
    return float(num1) - float(num2)

#This makes muliplication and division calculated before addition and subtraction
def getEquation(equation):
    i = 0                
    while len(equation) > i and hasProdDiv(equation):
        if equation[i] == '*' or equation[i] == '/':
            equation = process(equation, i)
        i=i+1
        
    i = 0
    while len(equation) > i and hasAddSub(equation):
        if equation[i] == '+' or equation[i] == '-':
            equation = process (equation, i)
        i=i+1

    return float(equation [0])

#This returns true or false based on the calculation
def hasProdDiv(equation):
    if '*' in equation:
        return True
    elif '/' in equation:
        return True
    else:
        return False   

def hasAddSub(equation):
    if '+' in equation:
        return True
    elif '-' in equation:
        return True
    else:
        return False
    
def process(equation, i):
    if equation[i] == '*':
        result = multiply(equation [i-1], equation [i+1])
    elif equation[i] == '/':  
        result = divide(equation [i-1], equation [i+1])
    elif equation[i] == '+':
        result = add(equation [i-1], equation [i+1])
    elif equation[i] == '-':
        result = subtract(equation [i-1], equation [i+1])
    for j in range(3):
        del equation [i-1]
    equation.insert(i-1, str(result))
    print(equation)
    return equation

#This initiates the input from the user  
def main():
    equation = input("Enter an equation (use spaces in between): ").split()
    result = getEquation(equation)
    print ("The result of the equation is", result)
   

main()



