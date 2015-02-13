import time
from random import randint
lista = "zxcvbnm"
gameOver = False
nombreJugador = raw_input("Ingresa tu nombre : ")
respuestas = ""
tiempo = 2.5
puntuacion = 0
print("La secuencia es : ")
while (gameOver == False):
    contador = 0
    respuestas += lista[randint(0,len(lista)-1)]
    for p in respuestas:
        print p
    time.sleep(tiempo)
    print " \n"*40 
    usuario = raw_input(nombreJugador + " escribe la secuencia : ")
    for i in range(len(respuestas)):
        if respuestas[i]==usuario[i]:
            contador+=1
    if not contador == len(respuestas):
        gameOver =True
    puntuacion += 10    
    tiempo -= .08
print("Has perdido, juego terminado")
print nombreJugador ,"tu puntuacion es :" , puntuacion