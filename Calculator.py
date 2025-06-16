def calculator():
    print("Simple Calculator")
    print("Operations available: +, -, *, /, %")
    print("Use '%' for two types of percent calculations:")
    print("1 → What percent one number is of another")
    print("2 → Find A% of B (like 10% of 50)")

    while True:
        num1 = float(input("\nEnter first number: "))
        operation = input("Enter operation (+, -, *, /, %): ")

        if operation == '%':
            choice = input("Enter 1 to calculate 'A is what percent of B'\n"
                           "Enter 2 to calculate 'A% of B' (like 20% of 100)\nYour choice : ")

            num2 = float(input("Enter second number: "))

            if choice == '1':
                if num2 == 0:
                    print("Error: Total cannot be zero.")
                else:
                    result = (num1 / num2) * 100
                    print(f"{num1} is {result:.2f}% of {num2}")

            elif choice == '2':
                result = (num1 * num2) / 100
                print(f"{num1}% of {num2} = {result} ")

            else:
                print("Invalid choice for % operation.")

        else:
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {num1} {operation} {num2} = {result}")

        # Ask to continue or exit (fixed here)
        print("")
        choice = input("Enter 1 to exit the calculator\n" 
                       '\n'
        "Enter 2 to use the calculator again: ")
        if choice == '1':
            print("Exiting the calculator. Goodbye!")
            break
calculator()