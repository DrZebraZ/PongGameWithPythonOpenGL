def valor(bola, x, y):
  bola["x"][0] += x
  bola["x"][1] += x
  bola["x"][2] += x
  bola["x"][3] += x
  bola["y"][0] += y
  bola["y"][1] += y
  bola["y"][2] += y
  bola["y"][3] += y
  return bola