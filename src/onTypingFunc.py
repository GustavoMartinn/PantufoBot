import src.global_variables as glob
import random

def typing(channel, user, when):

  #todo estudar python time library e refatorar
  if int(str(when)[11:13])-3 >= 0:
    hora = str(int(str(when)[11:13])-3)
  else:
    if int(str(when)[11:13])-3 == -3:
      hora = 21
    elif int(str(when)[11:13])-3 == -2:
      hora = 22
    elif int(str(when)[11:13])-3 == -1:
      hora = 23
  restoHora = str(when)[14:]
  #

  if (str(user) == glob.bernardo):
    rand = random.randint(1, 10)
    if (rand == 10):
      return('Vai estudar bernardo vagabundo')
  elif ((str(user) == glob.nath)) and (int(hora) >= 3 and int(hora) <= 6):
    rand = random.randint(1, 8)
    if (rand == 8):
      return('Nath, vai dormi, ja são ' + hora + ':' + restoHora)