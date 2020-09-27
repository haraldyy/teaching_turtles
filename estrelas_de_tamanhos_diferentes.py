from turtle import *

shape("turtle")
#Isso vai desenhar uma estrela cinza clara em um fundo azul escuro
bgcolor("MidnightBlue")
def estrela(tamanho,cor):
    color(cor)
    pendown()
    begin_fill()

#desenha a forma da estrela
    for side in range(5):
        forward(tamanho)
        left(144)
    end_fill()
    penup()
estrela(100, "Green")
penup()
right(90)
forward(100)
estrela(75,"Cyan")
left(90)
forward(100)
estrela(125, "Brown")
hideturtle()
done()
