def add(num1v, num2v):
  return num1v + num2v

def substract(num1v, num2v):
  return num1v - num2v

def multiply(num1v, num2v):
  return num1v * num2v

def divide(num1v, num2v):
  if num2v == 0:
    print("You can't divide by 0")
  else:
    return num1v / num2v

print("Simple Calculator")
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")