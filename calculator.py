print("Simple calculator")
print("Chose an operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number of the operation (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "1":
    result = num1 + num2
    print("Result:", result)
elif choice  == "2":
    result = num1 - num2
    print("Result:", result)
elif choice == "3":
    result = num1 * num2
    print("Result:", result)
elif choice == "4":
    if num2 == 0:
        print("Error: cannot devide by zero")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid unput")