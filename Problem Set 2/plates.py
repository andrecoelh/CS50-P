def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() == True:
        if len(s) == 6:
            if s[4].isalpha() == False:
                if s[5].isalpha() == False:
                    if s[1].isalpha() == True:
                        if s[2].isalpha() == True:
                            if s[3].isalpha() == True:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else: 
            return False
    else:
        return False

main()





































