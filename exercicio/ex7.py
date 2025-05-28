# and // or // not

entrada = input("[E] para entrar e [S] para sair: ")
senha = input("Senha: ") or "sem senha"


if (entrada=="E" or entrada=="e") and senha=="123":
    print("Entrou")
elif (entrada=="S" or entrada=="s") and senha=="123":
    print("saiu")
else:
    print("entrada ou senha incorreta")

print("\n========================\n")

senhaNova = input("digite uma nova senha: ")

if not senhaNova:
    print("Você não digitou uma senha")
else:
    print(f"Sua nova senha é: {senhaNova}")