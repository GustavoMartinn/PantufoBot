import random

def separarDados(dados):
  return dados.split(' ')

def fazerRolagem(dado):
  try:
    roll, tamanho = map(int, dado.split('d'))
  except Exception:
    print("erro")
    return('Format has to be in NdN!')
  result = ', '.join(str(random.randint(1, tamanho)) for r in range(roll))
  soma = eval('+ '.join(result.split(', ')))
  return result, soma, roll


def rolarDado(mensagem):
  dados = separarDados(mensagem)
  resultadoFinal = []
  somaFinal = 0
  qtdDados = 0
  for val in dados:
      resultado,soma, qtd = fazerRolagem(val)
      resultadoFinal.append(str(val)+"🎲: "+str(resultado)+" = "+str(soma))
      somaFinal += int(soma)
      qtdDados += qtd
  if(len(dados)>1):
    retorno = (('\n'.join(resultadoFinal))+"\nSoma total = "+str(somaFinal))
  elif(qtdDados>1):
    retorno = resultadoFinal[0]
  else:
    retorno = resultadoFinal[0].split('=')[0]
  return str(retorno)