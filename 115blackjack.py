#importar bibliotecas
import random

#criar variaveis e armazenar a soma acumulada das cartas
soma_cartas_j1 = 0
soma_cartas_j2 = 0

#tirando 3 cartas
for t in range (3):
    soma_cartas_j1 += random.randint(1,12)
    soma_cartas_j2 += random.randint(1,12)
    print(f'Soma do J1: {soma_cartas_j1} \nSoma do J2: {soma_cartas_j2}')
    print("-"*40)

#apurando o resultado
if soma_cartas_j1 <= 21 and soma_cartas_j1 > soma_cartas_j2:
    print("J1 VENCEU!")

if soma_cartas_j2 <= 21 and soma_cartas_j2 > soma_cartas_j1:
    print("J2 VENCEU!")