import requests
import json
from src.funcoes.calc import calcula
from src.funcoes.rolarDado import rolarDado

def get_quote():
  resposta = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(resposta.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def comandosBasicos(mensagem):
  #saudação
  if mensagem.startswith('&ola'):
    return ('Olá!')
  elif mensagem.startswith('pantufo ola'):
    return ('Olá!')
  #inspire
  elif mensagem.startswith('&inspire'):
    quote = get_quote()
    return (quote)
  #calcule
  elif mensagem.startswith('&calc'):
    return(calcula(mensagem[6:]))
  elif mensagem.startswith('pantufo calcule'):
    return(calcula(mensagem[16:]))
  #Rolagem de dados
  elif mensagem.startswith('&rolar'):
    return(str(rolarDado(mensagem[7:])))
  elif mensagem.startswith('&roll'):
    return(str(rolarDado(mensagem[6:])))
  elif mensagem.startswith('pantufo role'):
    return(str(rolarDado(mensagem[13:])))
  #superioridade 
  elif mensagem.startswith('pantufo > loritta'):
    return ('Sou mesmo 😎')
  #agradecimento
  if mensagem.startswith('&obrigado'):
    return ('magina')
  elif mensagem.startswith('pantufo obrigado'):
    return("magina")
  else:
    return('Desculpe, desconheço esse comando, aquele vagabundo do gustavo não me ensinou ainda')
