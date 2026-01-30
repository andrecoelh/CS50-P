def main():
        moedas_aceitas = [5, 10, 25]
        coke = 50
        tenho = 0
        devo = 0
        while tenho < coke:
                inserted = int(input("Insert Coin: "))
                if inserted in moedas_aceitas:
                        tenho += inserted
                        devo = coke - tenho
                        if devo <= 0:
                                break
                if devo > 0:
                        print("Amount Due:",devo)
                else:
                        print("Amount Due:",coke)
        change_owed = tenho - coke
        print("Change Owed:",change_owed)

main()