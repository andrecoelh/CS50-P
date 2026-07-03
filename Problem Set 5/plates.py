def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    check_letra = False

    for letter in s:
        if letter.isdigit():
            if check_letra == False:
                check_letra = True
                if letter == "0":
                    return False
        else:
            if check_letra == True:
                return False

    else:
        return True

if __name__ == "__main__":
    main()