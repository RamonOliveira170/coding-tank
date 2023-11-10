# Dicionários

dicionario = dict()
dicionario = {}

dicionario = {"Nome": "Luiz",
              "Idade": 52,
              "Altura": 1.28}

print(dicionario)

print(dicionario["Idade"])

dicionario["Programador"] = True

print(dicionario)

# Iterando sobre um dicionário

print()

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print()

print("peso" in dicionario)
print("Altura" in dicionario)