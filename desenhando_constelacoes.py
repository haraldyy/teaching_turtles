from turtle import *
from random import *
#uma função para mover a tartaruga para uma posição aleatória
def aleatoria():
    penup()
    setpos(randint(-400,400),randint(-400,400))
    pendown()

#uma função para desenhar uma estrela de um tamanho específico
def estrela(tamanho,cor):
    color(cor)
    pendown()
    begin_fill()
    for lado in range(5):
        left(144)
        forward(tamanho)
    end_fill()
    penup()
#uma função para desenhar uma pequena galaxia de estrela
def galaxia(nestrelas):
    cores=["#054385","#0275A6","827E01"]
    aleatoria()
#desenha varias pequenas estrelas coloridas
    for estrelas in range(nestrelas-1):
        estrela(randint(7,15),"white")
        pendown()
        left(randint(-90,90))
        forward(randint(30,70))
#agora desenhamos a ultima estrela
    estrela(randint(7,15),"white")

speed(11)

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#desenha 30 estrelas brancas aleatorias
for estrelas in range(30):
    aleatoria()
    estrela(randint(5,25),"white")

#desenhamos 3 pequenas galaxias de 40 estrelas
for galaxias in range(3):
    galaxia(40)

#desenha 2 constelações, cada uma com um numero aleatório de estrelas
for constelacoes in range(2):
    estrela(randint(4,7),"white")
hideturtle()
done()
print("Done")
