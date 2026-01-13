Task 1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


Output
Enter the first number: 10
Enter the second number: 5

Results:
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0


Task 2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name

print(f"Hello, {full_name}!Good Morning.")

Enter your first name: Supritha
Enter your last name: Sanjeev
Hello, Supritha Sanjeev!Good Morning.
