#CODIGO JR
numeros = [1, 2, 2, 3, 3, 4]
unicos = []

for n in numeros:
    if n not in unicos:
        unicos.append(n)


#CODIGO SR
unicos = list(set(numeros))
