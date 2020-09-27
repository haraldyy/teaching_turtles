from turtle import *

shape("turtle")
#Isso vai desenhar uma estrela cinza clara em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")
def estrela():
    pendown()
    begin_fill()

#desenha a forma da estrela
    for side in range(5):
        forward(50)
        left(144)
    end_fill()
    penup()
estrela()
forward(100)
estrela()
forward(50)
right(100)
forward(100)
pendown()
for i in range(160):
    forward(1)
    right(1)
done()
