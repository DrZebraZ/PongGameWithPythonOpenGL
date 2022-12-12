import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from draw import desenha
from somaBola import valor
from decideAngulo import decideAngulo


def main():
  
    pygame.init()
        
    windowSize = (1120, 600)
    
    pygame.display.set_mode(windowSize, DOUBLEBUF | OPENGL)
    gluPerspective(45, (windowSize[0] / windowSize[1]), 0.1, 70.0)
    glTranslatef(0.0, 0.0, -50)
    glClearColor(0,0,0,1)
    pygame.display.set_caption("PONG")
    
    campoX=40
    campoY1=20
    campoY2=25
    
    p1y = 0
    p2y = 0

    players={
      0:{"score":0, "pos":(-36,3,-35, 3, -35,-3,-36,-3)},
      1:{"score":0, "pos":(36, 3, 35, 3, 35, -3,36, -3)},
    }

    campo = [
      (-campoX, campoY2, campoX, campoY2, campoX, campoY1, -campoX, campoY1), 
      (-campoX, -campoY1, campoX, -campoY1, campoX, -campoY2, -campoX, -campoY2), 
      (-0.5, campoY1, 0.5, campoY1, 0.5, -campoY1, -0.5, -campoY1)
      ]

    bola = {"x":[-0.5,0.5,0.5,-0.5], "y":[0.5, 0.5,-0.5,-0.5]}

    x=0
    y=0
    angulo=1

    continuar = True
    
    while continuar:
      pygame.display.set_caption("PONG " + str(players[0]["score"]) + " X " + str(players[1]["score"]))
      for evento in pygame.event.get():
          if(evento.type == pygame.QUIT):
              continuar = False
          if(evento.type == pygame.KEYDOWN):
              if(evento.key == pygame.K_ESCAPE):
                  continuar = False
              if(evento.key == pygame.K_UP):
                if (p2y < 17):
                  p2y += 2
              if(evento.key == pygame.K_DOWN):
                if (p2y > -17):  
                  p2y += -2
              if(evento.key == pygame.K_w):
                if (p1y < 17):
                  p1y += 2
              if(evento.key == pygame.K_s):
                if(p1y > - 17):
                  p1y -= 2                    
    
      desenha(players, p1y, p2y, bola, campo)
      
      pygame.display.flip()
      
      if (y >= campoY1 or y <= -campoY1 or x>=campoX-5 or x<= -(campoX-5)):
        angulo = decideAngulo(angulo, x, y, p1y, p2y, campoX, campoY1)
          
      if angulo == 0:
        bola = valor(bola, +1, +1)
        x+=1
        y+=1
      elif angulo == 1:
        bola = valor(bola, -1, +1)
        x-=1
        y+=1
      elif angulo == 2:
        bola = valor(bola, -1, -1)
        x-=1
        y-=1
      elif angulo == 3:
        bola = valor(bola, +1, -1)
        x+=1
        y-=1
      elif angulo == 4:
        players[0]["score"]+=1
        print(str(players[0]["score"]) + " X " + str(players[1]["score"]))
        angulo = 0
        x=0
        y=0
        bola["x"]=[-0.5,0.5,0.5,-0.5]
        bola["y"]=[0.5, 0.5,-0.5,-0.5]
        if players[0]["score"] == 3:
          print("player 1 WINS")
          continuar = False
      elif angulo == 5:
        players[1]["score"]+=1
        print(str(players[0]["score"]) + " X " + str(players[1]["score"]))
        angulo = 1
        x = 0
        y = 0
        bola["x"]=[-0.5,0.5,0.5,-0.5]
        bola["y"]=[0.5, 0.5,-0.5,-0.5]
        if players[1]["score"] == 3:
          print("player 2 WINS")
          continuar = False
      
      pygame.time.wait(50)
main()
