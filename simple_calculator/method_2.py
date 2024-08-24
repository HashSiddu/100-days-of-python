
import art



def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2 == 0:
        return "Error" 
        
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    
    print(art.logo)
        
    first_number = float(input("enter the first number "))
    
    should_accumulate = True
    while should_accumulate:
        
        for symbol in operations:
            print(symbol)
        operation  = input("pick the operstion ")
        if operation not in operations:
            print("you entered invalid operation ")
            continue
        second_number = float(input("Ente the second number "))
        
            
        result = operations[operation](first_number,second_number)
        print(f"{first_number} {second_number}={result}")

        choice = input(f"type 'y' to calculate the with {result} or type 'no' to restart ")
        if choice == 'y':
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()   

calculator()