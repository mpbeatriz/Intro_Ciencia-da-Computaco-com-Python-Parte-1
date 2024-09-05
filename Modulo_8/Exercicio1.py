''' Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove.
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada. '''

# RESPOTA 1
def remove_repetidos(lista: list) -> list:
    i = len(lista) - 1
    while (i >= 0): 
        if lista.count(lista[i]) > 1:
            lista.remove(lista[i])
        i = i - 1
    lista.sort()
    return lista

# RESPOSTA 2
def remove_repetidos(lista: list) -> list:
     return list(set(lista))
