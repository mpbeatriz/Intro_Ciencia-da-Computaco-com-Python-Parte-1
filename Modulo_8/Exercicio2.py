''' Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros
e devolve um número inteiro correspondente à soma dos elementos da lista recebida.'''

# RESPOSTA 1
def soma_elementos(lista: list) -> int:         
    i = len(lista) - 1
    soma = 0                                        
    while (i >= 0):            
        e = lista[i]            
        soma = soma + e  
        i = i-1
    return soma

# RESPOSTA 2
def soma_elementos(lista: list) -> int:
    soma = 0
    for i in lista:
        soma += i
    return soma
