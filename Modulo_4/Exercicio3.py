''' Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.'''

a = int(input("Digite um número inteiro: "))
a = str(a)
b = list(a)
	
soma = 0
for i in b:
    i = int(i)
    soma += i

print(soma)
