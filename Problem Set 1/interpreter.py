def main():
    expression = input("Expression: ").strip().lower().split()
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    elif y == "*":
        print(x * z)
main()