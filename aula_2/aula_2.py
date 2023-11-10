# Estruturas condicionais

idade = 23

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

media = float(input("Informe a média do estudante: "))

if media >= 7:
    print(media, "Você foi aprovado.")
elif media >= 5:
    print(media, "Você está em recuperação.")
else:
    print(media, "Você foi reprovado(a).")

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print("Aprovado")
else:
    print("Reprovado")

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente...")

    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Parabens, você acertou!")

# estrutura com contador

contador = 0

while contador < 5:
    print(contador)
    contador += 1

    