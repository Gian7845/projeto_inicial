import math
import decimal

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Insira um numero: "))
# num2 = int(input("Insira outro numero: "))
# resultado = num1 + num2
# print ("A soma entre", num1,"+", num2, "é igual á:", resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num1 = int(input("Insira um numero inteiro: "))
# resultado = num1 % 5
# print("O resultado do resto da divisão de", num1,"* 5, é igual á:", resultado)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input("Insira um numero: "))
# num2 = int(input("Insira outro numero: "))
# resultado = num1 * num2
# print("A multiplicação entre", num1, "x", num2, "é:", resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input("Insira um numero inteiro: "))
# num2 = int(input("Insira outro numero inteiro: "))
# resultado = int(num1 / num2)
# print("A divisão entre", num1, "/", num2, "é:", resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num1 = int(input("Informe um numero inteiro: "))
# resultado = num1 ** 2
# print(num1, "elevado ao quadrado é:", resultado)


# #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input("Insira um numero flutuante: "))
# num2 = float(input("Insira outro numero flutuante: "))
# resultado = num1 + num2
# print("A soma entre", num1, "+", num2, "é igual á:", resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Insira um numero flutuante: "))
# num2 = float(input("Insira outro numero flutuante: "))
# soma = num1 + num2 
# media = soma / 2
# print("A media entre", num1, "e", num2, "é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num1 = float(input("Insira um numero flutuante: "))
# expoente = int(input("Insira um expoente: "))
# resultado = num1 ** expoente
# print(f"{num1} elevado a {expoente} é igual á: {resultado: .2f}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("insira uma temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) +32
# print(f"A temperatura de {celsius}ºC, em fahrenheit é: {fahrenheit:.2f}")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
def truncate(number, decimals=0):
    factor = 10 ** decimals
    return int(number * factor) / factor

raio = float(input("Informe o raio do círculo: "))
area = math.pi * raio**2
print("Área do círculo (truncada em 4 casas):", truncate(area, 2))


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação