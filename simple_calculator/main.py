
           
import art
print(art.logo)


# Simple calculator

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def first_number_fun():
    first_number = float(input("Enter the first number: "))
    return first_number

calculation_complete = True
final_value = None

while calculation_complete:
    # If final_value is None, ask for a new first number
    if final_value is None:
        first_number = first_number_fun()
    else:
        first_number = final_value  # Use the previous result

    # Display available operations
    print("Available operations:")
    for symbol in operations:
        print(symbol)

    operation = input("Pick an operation: ")
    
    # Check if the operation is valid
    if operation not in operations:
        print("Invalid operation. Please try again.")
        continue  # Skip to the next iteration of the loop

    second_number = float(input("Enter the second number: "))  # Convert to float
    result = operations[operation](first_number, second_number)
    print("Result:", result)

    continue_or_not = input("If you want to continue working with the previous result, type 'y'. If you want to enter a new first number, type 'n': ").lower()
    if continue_or_not == 'y':
        final_value = result  # Store the result for the next calculation
    elif continue_or_not == 'n':
        final_value = None  # Reset final_value to ask for a new first number
