"""  
Jogo no PyGame 02
Implementar um programa em Python com a biblioteca pygame que desenhe 
círculos "mágicos" na tela ao clicar com o mouse.
Esse código é apenas para analisar e explicar.
"""
import  pygame as py # Esta linha importa a biblioteca pygame e foi renomeada com o apelido PY, para facilitar ao referenciar funcoes e classes da biblioteca
size = (500, 400) # Define uma TUPLA chamada "size" com as dimensoes da tela do jogo - 500 pixel(largura), 400pxls(altura)
screen = py.display.set_mode(size) #para criar uma janela de exibição no pygame com as dimensoes especificadas em "size", e atribui essa janela a  variavel

while True: # Inicia um loop infinito ate que o jogo seja encerrado.
    for ev in py.event.get(): #ITERA sobre todos os eventos pygame que ocorreram desde a última vez que esta linha foi executada. Os eventos são obtidos através da função py.event.get().
        if ev.type == py.MOUSEBUTTONUP: # Verifica se o tipo de evento é um clique de mouse solto.(quando o botao do mouse é pressionado e depois solto)
            pos = py.mouse.get_pos() # Obtem a posicao atual do cursor do mouse na tela e armazena ela na variavel - "pos"
            col = (0, 255, 255) # Define uma cor para o circulo que sera desenhado. A cor é azul ciano representado pela TUPLA RGB(0,255,255) - 0 - ausencia de vermelho e 255 - maxima intensidade de verde e azul
            py.draw.circle(     #Desenha um circulo na superficie da tela("Screen") na posicao especificada por "pos".(..)
                screen, col, pos, 20, 5 #(..) Com raio de 20pxls, utilizando a cor especificada por "col"
            )                         # (..) Com uma espessura de linha de 5pxls
            py.display.update() # Atualiza a tela do jogo para mostrar o recém circulo desenhado