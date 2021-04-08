import random
import src.global_variables as glob

def separarDados(dados):
  return dados.split(' ')

def fazerRolagem(dado,vies):
  try:
    roll, tamanho = map(int, dado.split('d'))
  except Exception:
    print("erro")
    return('Format has to be in NdN!')
  result = ', '.join(str(gerarNumero(tamanho,vies)) for r in range(roll))
  soma = eval('+ '.join(result.split(', ')))
  return result, soma, roll

def gerarVies(autor):
  autor = str(autor)
  if(autor == glob.murilo or autor == glob.gustavo):
    vies = 10
  elif(autor == glob.gui):
    vies = -10
  else:
    vies = 0
  print (vies)
  return vies

def gerarNumero(tamanho,vies):
  var = random.randint(1, tamanho)+vies
  resultado = tamanho if var > tamanho else var
  return resultado

def rolarDado(mensagem,autor):
  dados = separarDados(mensagem)
  resultadoFinal = []
  somaFinal = 0
  qtdDados = 0
  for val in dados:
      resultado,soma, qtd = fazerRolagem(val,gerarVies(autor))
      resultadoFinal.append(str(val)+"🎲: "+str(resultado)+" = "+str(soma))
      somaFinal += int(soma)
      qtdDados += qtd
      if(qtdDados>1000):
        return "Você precisa de tantos dados? :upside_down:"
  if(len(dados)>1):
    retorno = (('\n'.join(resultadoFinal))+"\nSoma total = "+str(somaFinal))
  elif(qtdDados>1):
    retorno = resultadoFinal[0]
  else:
    retorno = resultadoFinal[0].split('=')[0]
  return str(retorno)
    