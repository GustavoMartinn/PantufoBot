import math

def calcula(mensagem):
  resultado = 0
  try: 
    resultado = (eval(mensagem))
  except Exception as e:
    if(str(e) == "division by zero"):
      if(mensagem == "0/0" or mensagem == '0 / 0'):
        resultado = "1/2"
      else:
        resultado = "Infinito"
    else:
      resultado = 'Entrada invalida'
    print(e)
  return resultado