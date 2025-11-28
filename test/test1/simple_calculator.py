# Define operations using functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Store operations in a dictionary
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

# History list to keep track of all calculations
history = []

def display_history():
    if history:
        print("\nCalculation History:")
        for idx, (operation, num1, num2, result) in enumerate(history, 1):
            print(f"{idx}. {num1} {operation} {num2} = {result}")
    else:
        print("No calculations yet.")

def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose the operation you'd like to perform:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    while True:
        try:
            choice = input("Enter choice (1/2/3/4), 'history' to view calculations, or 'exit' to quit: ").strip()
            
            if choice.lower() == 'exit':
                print("Goodbye!")
                break
            elif choice.lower() == 'history':
                display_history()
                continue
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid input. Please select a valid option.")
                continue
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the calculation using the dictionary of operations
            result = operations[choice](num1, num2)
            
            # Save the operation and result in the history list
            if choice == '1':
                operation = '+'
            elif choice == '2':
                operation = '-'
            elif choice == '3':
                operation = '*'
            elif choice == '4':
                operation = '/'
            
            history.append((operation, num1, num2, result))
            print(f"The result is: {result}")
        
        except ValueError:
            print("Invalid number input. Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
