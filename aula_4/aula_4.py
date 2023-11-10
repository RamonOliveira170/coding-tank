# Listas

notas = [7.9, 9.7, 8.2]

lista = []
lista = list()
lista =[25, "Matheus", True, 4.543]

lista_de_listas = [10, [1, 2, 3], []]


# Fatiamento

lista =[25, "Matheus", True, 4.543]

print("Segundo elemento da lista", lista[1])

print("Ultimo elemento da lista", lista[-1])

# Slices

lista = [10, 20, 30, 40, 50, 60, 70]

print(lista[0:3])

print(lista[3:])

print(lista[0::2])

# Iteração com FOR

for elemento in lista:
    print(elemento)

# Utilizando os índices

print("Comprimento da lista:", len(lista))

for i in range(len(lista)):
    print(i, "-", lista[i])

print()

# Métodos de listas

lista = [1, 3, 12, 8, 2]

print(lista)

lista.append(5)

print("Lista após o append:", lista)

lista.insert(2, 10)

print("Lista após o insert:", lista)

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Lista após o extend:", lista)

lista.pop()

print("Lista após o pop():", lista)

lista.pop(0)

print("Lista após o pop(0):", lista)

lista.remove(2)

print("Lista após o remove:", lista)

print("Quantidade de 2 na lista:", lista.count(2))

print("Indice do elemento 12:", lista.index(12))

lista.sort()

print("Lista ordenada:", lista)

lista.sort(reverse=True)

print("Lista com ordenação decrescente:", lista)

print("Soma dos elementos da lista:", sum(lista))

print("Maior valor da lista:", max(lista))

print("Menor valor da lista:", min(lista))
