#CÓDIGO JR
alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Bruno", "nota": 6}
]

def pegar_nota(aluno):
    return aluno["nota"]

ordenados = sorted(alunos, key=pegar_nota)

#CÓDIGO SR
ordenados = sorted(alunos, key=lambda a: a["nota"])
