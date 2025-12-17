#CODIGO JUNIOR
idade = 19

if idade >= 18:
    print("A pessoa é maior de idade")
else:
    print("É de menor")

#CODIGO SENIOR
def idade_check (idade):
    return 'Maior de idade' if idade >= 18 else 'Menor'

print(idade_check(19))
