# Criação de Funções

def saudacao(nome="Sem nome"):
    print(f"Seja bem vindo {nome}!")

saudacao("Matheus")

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(10, 50)

print("O resultado da soma é:", resultado)

def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "Não foi possivel realizar a operação."

resultado = calculadora(3, 5, "*")

print(resultado)