'''Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:
Exemplo 1:
Entrada de Dados:
Digite um número inteiro: 78615
Saída de Dados:
O dígito das dezenas é 1'''

numero = input("Digite um número inteiro: ")

dez = int(numero) // 10 % 10

print ("O dígito das dezenas é", dez)
