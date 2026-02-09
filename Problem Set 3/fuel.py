def main():
    while True:
        fraction = input("Fraction: ").strip().split("/")
        percent = convert(fraction)

        if percent is None:
            continue
        else:
            break

    if percent == 0:
        print("E")
    elif percent == 100:
        print("F")
    else:
        print(f"{percent}%")


def convert(fraction):
    while True:
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            z = int((x / y) * 100)
        except (ZeroDivisionError, ValueError, IndexError):
            return None
        else:
            return z


main()
