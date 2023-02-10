import discord
from discord import app_commands
from discord.ext import commands
import random
import requests
import scrapy
import discord_emoji

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",
                      case_insensitive=True,
                      intents=intents)


@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))


@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')


@client.command()
async def filme(ctx):
  name = 'imdb'
  start_urls = ['http://imdb.com/']
  filmes = []

  def parse(self, response):
    x = random.randint(1, 250)
    for filmes in response.css('.titleColumn'):
      filme = {
        titulo: filmes.css(f'tr:nth-child({x}).titleColumn a::text'),
        ano: filmes.css(f'tr:nth-child({x}).secondaryInfo ::text'),
        nota: response.css(f'tr:nth-child({x}) strong::text'),
      }
      filmes.append(filme)

      print(filme)

  for filme in filmes:
    await ctx.send(f"{filme['titulo']} {filme['ano']} {filme['nota']}")


@client.command()
async def dado(ctx, numero):
  variavel = random.randint(1, int(numero))
  await ctx.send(f'{variavel}')


@client.command()
async def toninho(ctx):
  await ctx.send('peida nao toninho {}{}'.format(
    discord_emoji.to_unicode(":face_with_hand_over_mouth:"),
    discord_emoji.to_unicode(":zany_face:")))


@client.command()
async def gabi(ctx):
  await ctx.send('idai gabi')


@client.command()
async def dolar(ctx):
  padrao = float('5.1322')
  requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
  requisicao_dic = requisicao.json()
  cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
  porcentagem = cotacao_dolar * (1 / padrao)
  if (cotacao_dolar > padrao):
    await ctx.send(
      f"A cotação atual do dólar é R$ {cotacao_dolar}; houve um aumento de {porcentagem}%"
      .replace('.', ','))
  elif (cotacao_dolar < padrao):
    await ctx.send(
      f"A cotação atual do dólar é R$ {cotacao_dolar}; houve um decréscimo de {porcentagem}%"
      .replace('.', ','))


@client.command()
async def desenho(ctx):
  aleat = random.randint(1, 18)
  if (aleat == 1):
    await ctx.send('Desenhe um fantasma.')
  elif (aleat == 2):
    await ctx.send('Desenhe uma pequena árvore bonsai.')
  elif (aleat == 3):
    await ctx.send('Desenhe um elfo.')
  elif (aleat == 4):
    await ctx.send('Desenhe um polvo humanóide de terno.')
  elif (aleat == 5):
    await ctx.send('Desenhe uma tartaruga marinha.')
  elif (aleat == 6):
    await ctx.send('Desenhe um gigante feito de pedra.')
  elif (aleat == 7):
    await ctx.send('Desenhe uma abóbora de halloween.')
  elif (aleat == 8):
    await ctx.send('Desenhe um espantalho.')
  elif (aleat == 9):
    await ctx.send('Desenhe algo relacionado à última emoção que sentiu.')
  elif (aleat == 10):
    await ctx.send('Desenhe um robô humanóide futurístico.')
  elif (aleat == 11):
    await ctx.send('Faça uma caricatura de si mesmo(a).')
  elif (aleat == 12):
    await ctx.send('Desenhe espelhos de diferentes ângulos.')
  elif (aleat == 13):
    await ctx.send('Rabisque um autorretrato no reflexo de uma colher.')
  elif (aleat == 14):
    await ctx.send('Ilustre a vista de uma janela.')
  elif (aleat == 15):
    await ctx.send('Esboce as nuvens.')
  elif (aleat == 16):
    await ctx.send('Combine formas de animais e faça uma criatura mítica.')
  elif (aleat == 17):
    await ctx.send('Dê um rosto para o personagem de um livro que você ama.')
  elif (aleat == 18):
    await ctx.send('Retrate uma cena para sua música favorita.')


@client.command()
async def fato(ctx):
  rand = random.randint(1, 18)
  if (rand == 1):
    await ctx.send(
      'Há mais estrelas no universo do que grãos de areia em todas as praias da Terra.'
    )
  elif (rand == 2):
    await ctx.send('Há cerca de 2 trilhões de galáxias no universo.')
  elif (rand == 3):
    await ctx.send('Ninguém entende a mecânica quântica.')
  elif (rand == 4):
    await ctx.send(
      'Se o sistema solar fosse uma piscina, Saturno seria o único planeta que boiaria.'
    )
  elif (rand == 5):
    await ctx.send(
      'Há um princípio científico-filosófico que diz que, dentre várias hipóteses que tentam explicar um fato, devemos escolher a mais simples. Essa é a navalha de Ockham.'
    )
  elif (rand == 6):
    await ctx.send('O planeta mais quente do sistema solar não é mercúrio.')
  elif (rand == 7):
    await ctx.send(
      'Quanto mais uma coisa se parece com um ser humano, mais desenvolvemos afeto sobre aquela coisa.'
    )
  elif (rand == 8):
    await ctx.send(
      'A temperatura do espaço é cerca de -270° C, mas não sentiríamos frio no vácuo.'
    )
  elif (rand == 9):
    await ctx.send(
      'Há uma coisa mais forte do que a gravidade de um buraco negro: a força centrípeta de rotação dessa região.'
    )
  elif (rand == 10):
    await ctx.send('Vetores são um ótimo atalho!')
  elif (rand == 11):
    await ctx.send(
      'Elétrons são partículas fundamentais, mas prótons não o são.')
  elif (rand == 12):
    await ctx.send('Algumas pessoas vêem um rosto na lua.')
  elif (rand == 13):
    await ctx.send(
      'Se você passasse um picossegundo (10^-12 s) no núcleo do sol, todos os seus órgãos seriam queimados à 25° C.'
    )
  elif (rand == 14):
    await ctx.send(
      'O tempo de Planck é o tempo passado sobre o Big Bang a partir do qual as implicações da teoria da relatividade geral passaram a ser válidas. Este intervalo de tempo situa-se na ordem dos 10^-43 s.'
    )
  elif (rand == 15):
    await ctx.send(
      'Quando elétrons recebem energia, eles passam para uma nova camada de distribuição eletrônica. Durante a volta, eles emitem luz.'
    )
  elif (rand == 16):
    await ctx.send(
      'Einstein morreu sem aceitar a teoria quântica. Para ele, a sua ideia de relatividade bastava para explicar o universo.'
    )
  elif (rand == 17):
    await ctx.send(
      'Se misturássemos todos os elementos da tabela periódica, o resultado seria o chamado "glúon de plasma" (o que os cientistas acreditam que saiu do Big Bang), ou plutônio em chamas.'
    )
  elif (rand == 18):
    await ctx.send(
      'Não é possível saber com exatidão o momento (massa x velocidade) e a posição de uma partícula ao mesmo tempo. Esse é o chamado Princípio da Incerteza de Heisenberg.'
    )


@client.command()
async def info(ctx):
  await ctx.send(
    'Olá! Eu sou o Esporádico. Para utilizar os meus comandos, digite o prefixo "!". No momento, tenho alguns comandos que utilizam da pseudoaleatoriedade para funcionar.'
  )


@client.command()
async def flip(ctx):
  aleatorio = random.randint(1, 6)
  divisao = int(aleatorio % 2)
  if (divisao == 1):
    await ctx.send('Cara!')
  else:
    await ctx.send('Coroa!')


@client.event
async def on_ready():
  print("O bot já está pronto!")
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Ei, {interaction.user.mention}! Esse é um comando slash.",
    ephemeral=True)


@client.tree.command(name="say")
@app_commands.describe(thing_to_say="O que eu devo fazer?")
async def say(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(
    f"{interaction.user.name} disse `{thing_to_say}`")


client.run('')
