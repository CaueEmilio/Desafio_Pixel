#!/usr/bin/env python

'''

Autor: Cauê Emilio de Moraes
Algoritmo para extração de dados de página web (link: http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar)
Atualização: 11/05/21

'''

from PIL import Image

imagem = Image.open('Syngenta.BMP','r')

valor_pixel = list(imagem.getdata())
#Antes da construção da contagem de pixels verdes, foram aferidos os valores das cores por meio de um "print(valor_pixel)" neste ponto do código  

print('A imagem está no formato "{0}", que é baseada em uma paleta de cores com variação entre 0 e 255, onde a cor preta possui o valor "0", a cor branca valor "255" e a cor verde valor "51"'.format(imagem.mode))

verde = 0
for pixel in valor_pixel:
    if pixel == 51: #conta apenas pixels verdes
        verde += 1

print('\nHá {} pixels verdes na imagem'.format(verde))
