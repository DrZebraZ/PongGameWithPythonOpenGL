import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def desenha(players, p1y, p2y, bola, campo):
  
    glClearColor(0, 0, 0, 0);
    glClear(GL_COLOR_BUFFER_BIT);    
    drawPlayers(players[0]["pos"], p1y)
    drawPlayers(players[1]["pos"], p2y)
    drawBola(bola["x"], bola["y"])
    drawQuads(campo[0])
    drawQuads(campo[1])
    drawQuads(campo[2])
    
def drawQuads(p):
    glColor3f(1, 1, 1);
    glPushMatrix();
    glBegin(GL_QUADS);
    glVertex2f(p[0], p[1]);
    glVertex2f(p[2], p[3]);
    glVertex2f(p[4], p[5]);
    glVertex2f(p[6], p[7]);
    glEnd();
    glPopMatrix();
    
def drawPlayers(p,y):
    glColor3f(1,1,1);
    glPushMatrix();
    glBegin(GL_QUADS);
    glVertex2f(p[0], p[1]+y);
    glVertex2f(p[2], p[3]+y);
    glVertex2f(p[4], p[5]+y);
    glVertex2f(p[6], p[7]+y);
    glEnd();
    glPopMatrix();
    
def drawBola(x, y):
    glColor3f(1,1,1);
    glPushMatrix();
    glBegin(GL_QUADS);
    glVertex2f(x[0], y[0]);
    glVertex2f(x[1], y[1]);
    glVertex2f(x[2], y[2]);
    glVertex2f(x[3], y[3]);
    glEnd();
    glPopMatrix();