'''Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo,
respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados),
uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.'''

l = int(input("Digite a largura: "))    
a = int(input("Digite a altura: "))     

linha = 0
coluna = 0

while coluna < a:
    while linha<l:
        linha = linha + l       
    coluna = coluna + a        
print ((('#' * linha) + '\n') * coluna) 
