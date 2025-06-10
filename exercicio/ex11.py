#constantes == CAPS
#variavel == low

velocidade_carro = 60
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_acima_radar_1 = (velocidade_carro > RADAR_1)
print(f"velocidade atual: {velocidade_carro} \n {vel_acima_radar_1}")
# Se o local do carro for maior ou igual a 99 E for menor ou igual a 101 == true
multa_radar_1 = (local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE))
print(f"Local atual: {local_carro} \n {multa_radar_1}")

if vel_acima_radar_1 and multa_radar_1:
    print("O carro foi multado no radar 1.")
else:
    print("O carro passou no radar 1.")