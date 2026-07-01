import inflect
p = inflect.engine()
names = []

while True:
    try:
        nome = input("Nomes: ")
        names.append(nome)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")