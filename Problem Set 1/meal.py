def main():
    time = input("What time is it? ")
    hora_final = convert(time) # salvo a variável "cuspida" em outra
    if 7 <= hora_final <= 8:
        print("breakfast time")
    elif 12 <= hora_final <= 13:
        print("lunch time")
    elif 18 <= hora_final <= 19:
        print("dinner time")
    else:
        print("")
def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    z = minutes / 60
    hora_conver = hours + z
    return hora_conver # a "caixinha" def convert "cuspiu" a variável hora_conver"
if __name__ == "__main__":
    main()