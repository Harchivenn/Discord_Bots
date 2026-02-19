import os
import discord
import logging

from wrpy import WordReference
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Permet de suivre les log dans le fichier 'discord.log'
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

wr = WordReference('fr', 'en')

@bot.event
async def on_ready():
    print(f"Moi,{bot.user.name}, pret a vioum !")

@bot.command()
async def hello(ctx, arg='you'):
    await ctx.send(f'Dev : Hello {arg}')

@bot.command()
async def translate(ctx, word, dest_language='en'):
    translation = wr.translate(word)
    word_target = translation['translations'][0]['entries'][0]['to_word'][0]['meaning'] #traduction principale
    #print(word_target)
    await ctx.send(f'{word} => {word_target} [{dest_language}]')
bot.run(token ,log_handler=handler, log_level=logging.DEBUG)

"""
{'word': 'teclado',
 'from_lang': 'Spanish',
 'to_lang': 'English',
 'url': 'https://www.wordreference.com/esen/teclado',
 'translations': [{'title': 'Principal Translations',
   'entries': [{'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': None, 'grammar': 'n'},
      {'meaning': 'keypad, touchpad', 'notes': None, 'grammar': 'n'}],
     'context': 'tablero con teclas',
     'from_example': 'No me funciona bien el teclado del portátil.',
     'to_example': ["The laptop keyboard isn't working well."]}]},
  {'title': 'Additional Translations',
   'entries': [{'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': 'music', 'grammar': 'n'}],
     'context': 'piano electrónico',
     'from_example': 'Aprendí a tocar el teclado de adolescente.',
     'to_example': ['I learned to play the keyboard when I was a teenager.']},
    {'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': 'piano', 'grammar': 'n'},
      {'meaning': 'keys', 'notes': None, 'grammar': 'npl'}],
     'context': 'teclas del piano',
     'from_example': 'Este señor viene a afinar el teclado del piano de cola.',
     'to_example': ["This man has come to fine tune the grand piano's keyboard"]}]},
  {'title': 'Compound Forms',
   'entries': [{'from_word': {'source': 'atajo de teclado',
      'grammar': 'nm + loc adj'},
     'to_word': [{'meaning': 'keyboard shortcut',
       'notes': None,
       'grammar': 'n'}],
     'context': 'Informática: grupo de teclas',
     'from_example': '¿Cuál es el atajo de teclado para guardar los cambios en un documento?',
     'to_example': []}]}]}
"""