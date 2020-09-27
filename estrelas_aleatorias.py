from turtle import *
from random import *
#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")
#Uma função para mover a tartaruga para uma posião aleatória
def posicao_aleatoria():
    penup()
    setpos(randint(-400,400),randint(-400,400))
    pendown()
#uma funcao para desenhar uma estrela de um tamanho específico
def estrela(tamanho,cor):
    color(cor)
    pendown()
    begin_fill()
    for  side in range(5):
        left(145)
        forward(tamanho)
    end_fill()
    penup()
for estrelas in range(30):
    posicao_aleatoria()
    estrela(randint(5,25),"White")
hideturtle()
done()
