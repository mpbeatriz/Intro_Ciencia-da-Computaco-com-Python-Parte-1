''' Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
como parâmetro e devolve o maior número primo menor ou igual ao número passado à função.'''


def eprimo(k):
    i = 2
    while (k>i):
        if (k % i == 0):
            return False
        i = i+1
    return True

def maior_primo(k):
    i = k
    while (eprimo(i) == False):
        i = i-1
    return i
    
