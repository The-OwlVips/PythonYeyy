# if / elif / else 

reinos = ["Wonderland", "Cinderellasburg", "Atlantis", "Corona"]
print("Escolha um reino para visitar!")
for i in range(len(reinos)):
    print(f"{reinos[i]}")

resposta = input("\n").lower()  # var.lower() == lowercase && var.upper() == uppercase
  
if resposta == "wonderland":
    print(f"Você escolheu {resposta}!!")
elif resposta == "cinderellasburg":
    print(f"Você escolheu {resposta}!!")
elif resposta == "atlantis":
    print(f"Você escolheu {resposta}!!")
elif resposta == "corona":
    print(f"Você escolheu {resposta}!!")
else:
    print("Você não escolheu nenhum dos reinos disponiveis :(")

