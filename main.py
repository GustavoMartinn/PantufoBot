import discord
import os

from keep_alive import keep_alive
from src.comandos import comandosBasicos
from src.wordsVerify import wordsVerify
from src.authorVerify import authorVerify
from src.onTypingFunc import typing
from src.mandarMensagem import mandarMensagem

client = discord.Client()

@client.event
async def on_ready():
  print('Logado como {0.user}'.format(client))

@client.event
async def on_typing(channel, user, when):
  try:
    await channel.send(typing(channel, user, when))
  except:
    return

@client.event
async def on_message(mensagem):
  if mensagem.author == client.user:
    return
  else:
    msg = mensagem.content.lower()
    
    #Comandos
    if msg.startswith('&'):
      await mandarMensagem(comandosBasicos(msg, mensagem.author), mensagem.channel)
    elif msg.startswith('pantufo'):
      await mandarMensagem(comandosBasicos(msg,mensagem.author), mensagem.channel)
    elif msg.startswith('é bolsonaro ou não é'):
      await mandarMensagem("ééééééé", mensagem.channel)
    elif msg.startswith('oi pantufo, td bem?'):
      await mandarMensagem("tudo otimo, e com vc?", mensagem.channel)
    elif msg.startswith('obrigado pantufo'):
      await mandarMensagem("magina", mensagem.channel)

    #Palavras
    for word in msg.split(' '):
      palavra = wordsVerify(word)
      if bool(palavra) ==  True:
        await mandarMensagem(palavra, mensagem.channel)
        return
    
    #Autor
    frase = authorVerify(mensagem)
    if frase != None:
      await mandarMensagem(frase, mensagem.channel)

keep_alive()
#TOKEN dado pelo Discord Developer Portal
client.run(os.getenv('TOKEN'))