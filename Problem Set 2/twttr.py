def main():
    abreviado = ""
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    abreviar = input("Input: ").strip()
    for letter in abreviar:
        if letter in vogais:
            abreviado += ""
        else:
            abreviado += letter
    print(abreviado)
main()
































