def decideAngulo(angulo, x, y, p1y, p2y, campoX, campoY):
  if angulo == 0:
    angulo = angulo0(angulo,x,y,p1y,p2y,campoX,campoY)
  elif angulo == 1:
    angulo = angulo1(angulo,x,y,p1y,p2y,campoX,campoY)
  elif angulo == 2:
    angulo = angulo2(angulo,x,y,p1y,p2y,campoX,campoY)
  elif angulo == 3:
    angulo = angulo3(angulo,x,y,p1y,p2y,campoX,campoY) 
  return angulo
  

def angulo0 (angulo, x, y, p1y, p2y, campoX, campoY):
  if (y>=campoY):
      angulo = 3
  elif (x>=campoX-5 and x<campoX):
    if ((y+1 in range(p2y-3, p2y+3)) or y-1 in range(p2y-3, p2y+3)):
      angulo = 1
    else:
      angulo = 4
  
  if (x >= campoX):
    angulo=4
    
  return angulo
  
  
def angulo1 (angulo, x, y, p1y, p2y, campoX, campoY):
  if (y>=campoY):
    angulo = 2
    
  elif (x<=-(campoX-5) and x>-campoX):
    if ((y+1 in range(p1y-3, p1y+3)) or y-1 in range(p1y-3, p1y+3)):
      angulo = 0
    else:
      angulo = 5
  
  if (x <= -campoX):
    angulo = 5
    
  return angulo


def angulo2 (angulo, x, y, p1y, p2y, campoX, campoY):
  
  if (y<=-campoY):
    angulo = 1
    
  elif (x<=-(campoX-5) and x>-campoX):
    if ((y+1 in range(p1y-3, p1y+3)) or y-1 in range(p1y-3, p1y+3)):
      angulo = 3
    else:
      angulo = 5
  
  if (x <= -campoX):
    angulo = 5
    
  return angulo


def angulo3 (angulo, x, y, p1y, p2y, campoX, campoY):
  if (y<=-campoY):
    angulo = 0
  elif(x>=campoX-5):
    if((y+1 in range(p2y-3, p2y+3)) or y-1 in range(p2y-3, p2y+3)):
      angulo = 2
    else:
      angulo = 4
      
  if (x>campoX):
    angulo = 4    
  
  return angulo