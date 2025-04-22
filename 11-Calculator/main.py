import art

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Operation to perform
operations = {
             "+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }

# main function 
def calculate():
    print(art.logo)
    do_calculate = True
    first_number = float(input("Enter the first number : "))

    # Restart Calculator or continue with previous calculation
    while do_calculate:
        print("Allowed operations :")
        for symbols in operations:
            print(symbols)
        operation_to_perform = input("Select the operation to perform : ")
        second_number = float(input("Enter the second number : "))
        answer = operations[operation_to_perform](first_number, second_number)
        print(f"{first_number} {operation_to_perform} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            first_number = answer
        else:
            do_calculate = False
            print("\n" * 50)
            calculate()

# Calling the main function 
calculate()