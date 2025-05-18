#input

nome = input("digite o seu nome: ")
print(f"O seu nome é: {nome} \n")

# Pokemon type /// fstring {variavel=} o igual faz com que exiba o nome e o valor :)

pikachu = "eletrico"
charmander = "fogo"
bulbasour = "grama"
squirtle = "água"

print("Escolha o seu primeiro pokemon!!")
print(f"{pikachu=}")
print(f"{squirtle=}")
print(f"{bulbasour=}")
print(f"{charmander=} \n")

starter = input("Qual você escolhe? ")

print(f"{nome} escolheu {starter}!!")