def main():
    greeting = input("Greeting: ").lower().strip()
    first = greeting[0]
    if "hello" in greeting:
        print("$0")
    elif first == "h":
        print("$20")
    else:
        print("$100")
main()