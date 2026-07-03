def shorten(text):
    resultado = ""

    for letra in text:
        if letra not in "aeiouAEIOU":
            resultado += letra

    return resultado


def main():
    texto = input("Input: ")
    print(shorten(texto))


if __name__ == "__main__":
    main()
