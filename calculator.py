print("🧮 Simple Calculator 🧮")

num1 = float(input("Pehla number: "))
op = input("Operation (+, -, *, /): ")
num2 = float(input("Doosra number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: 0 se divide nahi hota!"
else:
    result = "Galat operation!"

print(f"Result: {result}")