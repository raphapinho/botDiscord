import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Nós logamos com o usuário {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$olá"):
        await message.channel.send('opa, meu bom, tudo tranquilo?')

    if message.content.startswith('$help'):
        await message.channel.send('eu quero que tu se foda!!!')

    if message.content.startswith('$to mal'):
        await message.channel.send('foda-se?')
    
    if message.content.startswith('$gay'):
        while message.content.starswith != '$para': 
            message.channel.send('gay')

    

client.run('')#o token vai aqui