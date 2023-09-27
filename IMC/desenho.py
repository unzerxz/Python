import turtle
import random

tela = turtle.Screen()
tela.bgcolor("black")
tartaruga = turtle.Turtle()
tartaruga.speed(50)
tartaruga.width(2)


cores = ["red", "orange", "yellow", "green", "blue", "purple"]


def desenhar_espiral(num_segmentos, comprimento_inicial, angulo):
    for _ in range(num_segmentos):
        tartaruga.color(random.choice(cores))  
        tartaruga.forward(comprimento_inicial)
        tartaruga.right(angulo)
        comprimento_inicial += 5  #aumenta o comprimento inical em 5 pra dar a forma de espiral


desenhar_espiral(80, 20, 45) #numero de segmentos/ comprimento / angulo


tela.exitonclick()