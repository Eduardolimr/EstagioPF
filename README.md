# EstagioPF

### Problema 1
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', 
e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja 
repetição de valores na segunda lista.
## Solução
[prob1.py](https://github.com/Eduardolimr/EstagioPF/blob/main/prob1.py)
## Raciocínio
Para resolver esse problema eu decidi abordá-lo em duas etapas: converter a lista de dicionários em uma lista de listas para manusaá-la mais livremente e criar um Set(check no código) para lidar com as duplicatas. Depois disso, é só uma questão de iterar pela lista de listas e comparar se já existe um elemento com o mesmo nome na coleção Set.


### Problema 2
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registros ordenados por nome.
'''
Exemplo de arquivo:
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12
'''
## Solução
[prob2.py](https://github.com/Eduardolimr/EstagioPF/blob/main/prob2.py)
## Raciocínio
Para resolver esse problema usei a bibliotecas nativa do Python de csv pois ela já faz a conversão para os tipos do Python automaticamente, além de separar pelo delimitador. Usei o DictReader para converter a leitor de csv para um dicionário, e depois o ordenei usando a função sorted filtrando por nome na lista.
