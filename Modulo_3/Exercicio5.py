'''Receba 3 números inteiros na entrada e imprima "crescente"
se eles forem dados em ordem crescente. Caso contrário, imprima 
"não está em ordem crescente"'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

if numero1 <= numero2 <= numero3:
    print("Crescente.")
else:
    print("Não está em ordem crescente.")
