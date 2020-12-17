import csv
from operator import itemgetter

path = "./exemplo.csv"
listaOrdenada = []

with open(path, 'rb') as arq:
    texto = csv.DictReader(arq, delimiter=";")

    listaOrdenada = sorted(list(texto), key = lambda k: (k['nome']))
    for item in listaOrdenada:
        print(item)
