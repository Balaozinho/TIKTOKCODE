idades = [12, 15, 18, 20, 22]

#CÓDIGO JUNIOR
maiores = []
#for idade in idades:
#    if idade >= 18:
#        maiores.append(idade)

#CÓDIGO SENIOR
maiores = [i for i in idades if i >= 18]

print(maiores)