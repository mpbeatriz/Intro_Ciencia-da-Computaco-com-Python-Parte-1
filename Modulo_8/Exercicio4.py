'''Como pedido na primeira video-aula desta semana, escreva um programa que
recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa.
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.'''

# RESPOSTA 1
def lista_seq() -> int: 
    lista = []
    num = int(input("Digite um número: "))
    while num != 0:
        lista.append(num)
        num = int(input("Digite um número: "))
    lista.sort()

    for i in range(len(lista)):
        print(lista[i])
    return ''

# RESPOSTA 2
lista = []
numero = 1
while (numero != 0):
    numero = int(input("Digite um número (zero para fechar): "))
    lista.append(numero)
tamanho = len(lista) - 1


while (tamanho >= 0):
    if (tamanho == len(lista) - 1):
        print('')
    else:
        print(lista[tamanho])
    tamanho = tamanho - 1
