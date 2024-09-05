'''Receba um número inteiro positivo na entrada e imprima os n
primeiros números ímpares naturais.'''

n = int(input("Digite um número: "))
i = 1
impares = 0
while (impares<n):
    if (i % 2 != 0):
        print (i)
        impares = impares + 1    
    i = i+1
