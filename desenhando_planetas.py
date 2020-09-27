from turtle import *

shape("turtle")
color("WhiteSmoke")
bgcolor("MidnightBlue")

def planeta(tamanho,cor):
    for i in range(360):
        color(cor)
        forward(1)
        right(tamanho)

