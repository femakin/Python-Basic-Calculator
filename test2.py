#  A basic Python calculator that will run only in the console

# This function adds two numbers
def sum(a, b):
    return a + b

# This function subtracts two numbers
def difference(a, b):
    return a - b

# This function multiplies two numbers
def multiply(a, b):
    return a * b

# This function divides two numbers
def division(a, b):
    return a / b
def quit():
    return exit()


print("Welcom! Please select an Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = int(input("Pick from 1-4 above: "))
    
   # int(input('Enter the name of the player you wish to vote for'))
    # Check if choice is one of the four options
    if choice <= int('4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == int('1'):
            print(num1, "+", num2, "=", sum(num1, num2))

        elif choice == int('2'):
            print(num1, "-", num2, "=", difference(num1, num2))

        elif choice == int('3'):
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == int('4'):
            print(num1, "/", num2, "=", division(num1, num2))
            
        elif choice >= int('5'):
         #   print("Invalid Input", quit() )
         quit()
        break
    else:
            print("Wrong input..!!")
            
  #  else:
   #     print("Invalid Input", quit(num1, num2) )


