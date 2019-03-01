#this program generates a calculator
#McKinley Fox
#Project 1
#2019-02-25

# This allows for two numbers to be multiplied
def multiplication(x, y):
   return x * y

# This allows for two numbers to be divided
def division(x, y):
   return x / y

#this allows two numbers to be added
def addition(x, y):
    return x + y

# This allows for two numbers to be subtracted 
def subtraction(x, y):
   return x - y

#gives the user a choice of their function
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#correlates the function with the user's choice
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

