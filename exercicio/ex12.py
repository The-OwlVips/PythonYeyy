#is ou not is
#None

CANON = True
glassheart = True
print(glassheart is CANON)

#EU TENHO O PODER NAS MINHAS MÃOS AHAHAHHAHAHAHAHA

print("-"*30)
print("Exercicios")
print("-"*30)

""" 
    Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""
numero_str = (input("Informe um número inteiro: "))

try:
    numero = float(numero_str)
    if numero % 2 == 0:
        print("O número é par!")
    elif numero % 2 == 1:
        print("O número é ímpar")
    else:
        print("Você não digitou um número INTEIRO.")
except:
    print("Você não digitou um número.")

print("-"*30)
"""
    Faça um programa que pergunte a hora ao usuário e, com baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom Dia 0-11, Boa Tarde 12-17, Boa Noite 18-23
"""
horario_str = input("Informe o horário atual: ")

try:
    horario = float(horario_str)
    if horario >= 0 and horario <= 11.59:
        print("Bom Dia!")
    elif horario >= 12 and horario <= 17.59:
        print("Boa Tarde!")
    elif horario >= 18 and horario <= 23.59:
        print("Boa Noite!")
    else:
        print("Horário invalido")
except:
    print("Você não informou um horário")

print("-"*30)
"""
    Faça um programa que peça o nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; Se tiver 5-6 letras, escreva "Seu nome é normal"; Maior que 6 escreva "Seu nome é grande". 
"""
nome_str = input("Informe seu nome: ")

if nome_str is not None:
    if len(nome_str) <= 4:
        print("Seu nome é curto")
    elif len(nome_str) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é grande.")
else:
    print("Você não informou um nome.")

print("-"*30)