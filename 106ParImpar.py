import random

j1 = "Par"
j2 = "Ímpar"

nj1 = random.randint(1,10)
nj2 = random.randint(1,10)

resultado = nj1 + nj2
print(f'O resultado é: {resultado}')

if resultado %2 == 0:
    print(f'O vencedor é o Jogador 1, escolheu {j1}')
else:
    print(f'O vencedor é o Jogador 2, escolheu {j2}')

