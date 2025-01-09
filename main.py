# version: Python3
from DobotEDU import *
import cv2
import numpy as np

def VerificandoCor():

    camera = cv2.VideoCapture(1)

    if not camera.isOpened():
      exit()

    ret, img = camera.read()
    frame = cv2.blur(img,(5, 5))

    if ret:

      lower_yellow = (0, 140, 174)
      upper_yellow = (27, 178, 225)
      maskyellow = cv2.inRange(frame, lower_yellow, upper_yellow)

      lower_green = (20, 90, 50)
      upper_green = (35, 150, 85)
      maskgreen = cv2.inRange(frame, lower_green, upper_green)
      

      lower_red = (30, 25, 220)
      upper_red = (65, 50, 240)
      maskred = cv2.inRange(frame, lower_red, upper_red)

      lower_blue = (142, 74, 0)
      upper_blue = (217, 114, 0)
      maskblue = cv2.inRange(frame, lower_blue, upper_blue)

      cv2.waitKey(0)
      cv2.destroyAllWindows()
      camera.release()
      
      if np.any(maskred):
        return 1
      elif np.any(maskyellow):
        return 3
      elif np.any(maskblue):
        return 4
      elif np.any(maskgreen):
        return 2
      
    return 0

print(VerificandoCor())

def PegarBloco(X, Y, count):
  m_lite.set_ptpcmd(ptp_mode=2, x=X, y=Y, z=73.5, r=0)
  m_lite.set_ptpcmd(ptp_mode=2, x=X, y=Y, z=-38.5, r=0)
  
  m_lite.set_endeffector_suctioncup(enable=True, on=True)
  
  m_lite.set_ptpcmd(ptp_mode=2, x=X, y=Y, z=73.5, r=0)
  
  m_lite.set_ptpcmd(ptp_mode=2, x=270, y=0, z=73.5, r=0)
  m_lite.set_ptpcmd(ptp_mode=2, x=270, y=0, z=-36, r=0)
  
  m_lite.set_endeffector_suctioncup(enable=False, on=False)
  
  m_lite.set_ptpcmd(ptp_mode=2, x=220, y=0, z=30, r=0)
  
  cor = VerificandoCor()
  
  m_lite.set_ptpcmd(ptp_mode=2, x=270, y=0, z=30, r=0)
  m_lite.set_ptpcmd(ptp_mode=2, x=270, y=0, z=-40, r=0)
  
  m_lite.set_endeffector_suctioncup(enable=True, on=True)
  
  m_lite.set_ptpcmd(ptp_mode=2, x=270, y=0, z=73.5, r=0)
  
  if cor == 1:
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[0]*20, y=-130, z=73.5, r=0)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[0]*20, y=-130, z=-38.5, r=0)
    m_lite.set_endeffector_suctioncup(enable=False, on=False)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[0]*20, y=-130, z=73.5, r=0)
    count[0] += 1
  elif cor == 2:
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[1]*20, y=-110, z=73.5, r=0)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[1]*20, y=-110, z=-38.5, r=0)
    m_lite.set_endeffector_suctioncup(enable=False, on=False)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[1]*20, y=-110, z=73.5, r=0)
    count[1] += 1
  elif cor == 3:
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[2]*20, y=-90, z=73.5, r=0)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[2]*20, y=-90, z=-38.5, r=0)
    m_lite.set_endeffector_suctioncup(enable=False, on=False)
    m_lite.set_ptpcmd(ptp_mode=2, x=250+count[2]*20, y=-90, z=73.5, r=0)
    count[2] += 1
  elif cor == 4:
      m_lite.set_ptpcmd(ptp_mode=2, x=250+count[3]*20, y=-70, z=73.5, r=0)
      m_lite.set_ptpcmd(ptp_mode=2, x=250+count[3]*20, y=-70, z=-38.5, r=0)
      m_lite.set_endeffector_suctioncup(enable=False, on=False)
      m_lite.set_ptpcmd(ptp_mode=2, x=250+count[3]*20, y=-70, z=73.5, r=0)
      count[3] += 1

x = 270
y = 70

count = [1, 1, 1, 1]

m_lite.set_homecmd()

for i in range(4):
  for j in range(4):
    PegarBloco(x, y, count)
    y+=20
  y=70
  x+=20

m_lite.set_homecmd()
