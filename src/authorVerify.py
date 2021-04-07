import src.global_variables as glob

#pessoas
bernardo = glob.bernardo
gui = glob.gui
gustavo = glob.gustavo
#contadores
beCount = glob.contadorBe
guiCount = glob.contadorGui
guCount = glob.contadorGu

respostaUser = glob.respostaUser

def authorVerify(mensagem):
  global guiCount
  global beCount
  global guCount
  global respostaUser

  if (str(mensagem.author) == (gui)):
    if guiCount == respostaUser:
      guiCount = 0
      return ('É bolsonaro ou n é, gui?')
    guiCount += 1
  elif (str(mensagem.author) == (bernardo)):
    if beCount == respostaUser:
      beCount = 0
      return ('Vai estudar vagabundo')
    beCount += 1
  elif(str(mensagem.author)) ==  (gustavo):
    if guCount == respostaUser:
      guCount = 0
      return ('Oi lindo')
    guCount += 1