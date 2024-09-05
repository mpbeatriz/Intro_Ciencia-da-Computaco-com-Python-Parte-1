'''Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui
ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não". '''

def numero_adjacente(num: int) -> str:
    num = str(num)
    
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            return "sim"
    return "não"
