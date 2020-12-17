'''
Problema 1:
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', 
e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja 
repetição de valores na segunda lista.
'''

lista = [ 
    {
    "nome": "James",
    "ano": 1993
    },
    {
    "nome": "Jessie",
    "ano": 1995
    },
    {
    "nome": "Miau",
    "ano": 2005
    },
    {
    "nome": "Ash",
    "ano": 2003
    },
    {
    "nome": "James",
    "ano": 2010
    },
    {
    "nome": "Ash",
    "ano": 2018
    }
]

chaves = ['nome', 'ano']

listaNomes = []
check = set(listaNomes)

for item in lista:
    temp = list(map(item.get, chaves))
    if temp[0] in check:
        print("Item existente!")
    else:
        check.add(temp[0])
        listaNomes.append(temp[0])

print(listaNomes)
