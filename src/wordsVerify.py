import random

palavras_tristes = ["triste", "deprimido", "chateado"]

iniciar_inspiracao = [
  "Animo!!!",
  "Não desista!!!",
  "Voce é foda!!!"
]

def wordsVerify(word):
  if word == "gustavo":
    return('Gustavo? Aquele lindo?')
  elif word == "bernardo":
    return("Bernardo? Adoro aql gostoso")
  elif word in palavras_tristes:
    return(random.choice(iniciar_inspiracao))
  elif word == "bolsonaro":
    return ("É bolsonaro ou não é??")
  elif word == "gi":
    return ("Ô saudades da mãe da gi")
  else:
    return False
