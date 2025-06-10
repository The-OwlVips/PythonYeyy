#Try --> Tentar executar o codigo 
#Except --> Se ocorrer erro ao executar o codigo

# EXEMPLO

num_str = input("Informe um numero: ")

try:
    print("STR:", num_str)
    num_float = float(num_str)
    print("FLOAT:", num_float)
    print(f"O dobro de {num_str} é {num_float*2}")
except:
    print("O valor informado não é um numero")

print("-" * 30)
