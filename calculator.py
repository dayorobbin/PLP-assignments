#Define a function
def calculate(num1, num2, operation):
    if operation == '+': 
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error division by zero"
    else:
        return "Syntax error"
#Main program
def main():
    #user input
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    operation = input('Enter the operations:( +, -, *, /,):')
#Calculate and run the result
    result = calculate(num1,num2, operation)
    print(f"{num1} {operation} {num2} = {result}")
# Run the calculator
main()