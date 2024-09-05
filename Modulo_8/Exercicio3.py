'''Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros
e devolve um número inteiro correspondente ao maior valor presente na lista recebida.'''

# RESPOTA 1

def maior_elemento(list: lista) -> int:
    return max(lista)

# RESPOSTA 2

def maior_elemento(lista: list) -> int: 
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

# RESPOSTA 3

def maior_elemento(lista):
    maior = lista[0]
    i = 0
    while i < len(lista):
        if maior < lista[i]:
            maior = lista[i]
        i += 1
    return maior
