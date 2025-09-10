#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome =    input("Digite seu nome: ")
salario = int(input("Informe seu salario: "))
bonus =   float(input("Informe o valor do bonus: "))
kpi =  1000 + salario * bonus

print("Olá", nome , ', o seu bônus foi de:', kpi)
