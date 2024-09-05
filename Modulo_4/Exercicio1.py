'''
Escreva um programa que receba um número natural 'n'
na entrada e imprima 'n!' (fatorial) na saída.'''

n = int(input("Digite o valor de n: "))

fat = 1

while n > 1:
    fat = fat * n
    n = n-1
print(fat)
