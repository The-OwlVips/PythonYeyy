num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

if num1 > num2:
    print(f'o primeiro numero ({num1}) é maior que o segundo numero ({num2})')
elif num1 < num2:
    print(f'o primeiro numero ({num1}) é menor que o segundo numero ({num2})')
else:
    print('Os numeros são iguais')