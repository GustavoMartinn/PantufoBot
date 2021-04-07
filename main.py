import discord
import os
from keep_alive import keep_alive
from src.comandos import comandosBasicos
from src.wordsVerify import wordsVerify
from src.authorVerify import authorVerify
from src.onTypingFunc import typing

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
      try:
        await mensagem.channel.send(comandosBasicos(msg))
      except:
        print('Comando invalido')
      return
    elif msg.startswith('pantufo'):
      try:
        await mensagem.channel.send(comandosBasicos(msg))
      except:
        print('Comando invalido')
      return
    elif msg.startswith('é bolsonaro ou não é'):
      await mensagem.channel.send("ééééééé")
      return
    elif msg.startswith('obrigado pantufo'):
      await mensagem.channel.send("magina")
      return

    #Palavras
    for word in msg.split(' '):
      palavra = wordsVerify(word)
      if bool(palavra) ==  True:
        await mensagem.channel.send(palavra)
        return
    
    #Autor
    try:
      await mensagem.channel.send(authorVerify(mensagem))
    except:
      return

keep_alive()
client.run(os.getenv('TOKEN'))