def calculator():
    try:
        # Get user input
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        # Display the result
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
