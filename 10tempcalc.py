import datetime

formato = "%H:%M:%S"

def diff_tempo (t1, t2):
    tempo1 = datetime.datetime.strptime(t1, formato)
    tempo2 = datetime.datetime.strptime(t2, formato)
    return tempo2 - tempo1

tempo_inicio = '08:34:21'
tempo_final = '13:55:09'

diff = diff_tempo(tempo_inicio, tempo_final)
print(diff)