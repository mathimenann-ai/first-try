#---------- User-Defined Functions ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

if name == "main":
    print("===== Simple Calculator =====")
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice (1-5): ")

if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select 1-5.")


