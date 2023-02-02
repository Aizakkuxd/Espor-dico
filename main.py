import discord
from discord import app_commands
from discord.ext import commands
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",
                      case_insensitive=True,
                      intents=intents)


@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))


@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, @{ctx.author}')


@client.command()
async def dado(ctx, numero):
  variavel = random.randint(1, int(numero))
  await ctx.send(f'{variavel}')


@client.command()
async def toninho(ctx):
  await ctx.send('peida nao toninho')


@client.command()
async def gabi(ctx):
  await ctx.send('idai gabi')


@client.command()
async def desenho(ctx):
  aleat = random.randint(1, 10)
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


@client.command()
async def fato(ctx):
  rand = random.randint(1, 10)
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
