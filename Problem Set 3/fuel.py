def main():
    while True:
        fraction = input("Fraction: ").strip().split("/")
        percent = convert(fraction)

        if percent is None:
            continue
        else:
            break

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def convert(fraction):
    while True:
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            if x < 0 or y < 0:
                return None
            z = round((x / y) * 100)
            if z > 100:
                return None
        except (ZeroDivisionError, ValueError, IndexError):
            return None
        else:
            return z


main()