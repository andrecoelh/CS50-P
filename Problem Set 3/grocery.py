qtd = {}

while True:
    try:
        item = input().upper()
        if item in qtd:
            qtd[item] += 1
        else:
            qtd[item] = 1
    except EOFError:
        break

for item in sorted(qtd):
    print(qtd[item], item)
