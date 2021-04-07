import random

def rolarDado(mensagem):
  try:
    rolls, limit = map(int, mensagem.split('d'))
  except Exception:
    return('Format has to be in NdN!')

  result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
  soma = eval('+ '.join(result.split(', ')))
  if (rolls == 1):
    return('A rolagem resultou em: ' + result)
  else: 
    return('A soma dos dados rolados é: **' + str(soma) + '** Os dados rolados são: ' + result)