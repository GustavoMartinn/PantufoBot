class Mensagem(object):
  content: ""
  channel: ""

  def __init__(self, content, channel):
    self.content = content
    self.channel = channel

def MakeMensagem(content, channel):
  mensagem = Mensagem(content, channel)
  return mensagem

async def mandarMensagem(msg, channel):
  msg = MakeMensagem(msg, channel)
  conteudo = msg.content
  canal = msg.channel
  try:
    qtd = int(len(conteudo)/2000) + 1
    print(qtd)
    for i in range(0,qtd):
      if(i == qtd):
        await canal.send(conteudo[i*2000:(i+1)*2000])
        return
      await canal.send(conteudo[i*2000:(i+1)*2000])
  except Exception as e:
    print(e)
  return