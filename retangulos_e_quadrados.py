from turtle import *

shape("turtle")
#Isso vai desenhar uma estrela cinza clara em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")
def quadrado():
    for i in range(4):
        forward(100)
        right(90)
def retangulo():
    for i in range(2):
        right(90)
        forward(150)
        right(90)
        forward(90)
quadrado()
penup()
backward(250)
pendown()
left(90)
retangulo()

