'''Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.'''


largura = int(input("Digite a largura: ")) #10
altura = int(input("Digite a altura: ")) #5

linha = 1

while (linha <= altura):
    coluna = 1
    while (coluna <= largura): #(coluna <= )
        if coluna == 1 or coluna == largura or linha == 1 or linha == altura:
            print("#", end = '')
        else:
            print (' ', end = '')
        coluna = coluna + 1
    print()
    linha = linha + 1
