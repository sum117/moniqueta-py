import discord
from embeds import create_char_embed

bot_token = "MTAwMTI3NDMzNDA5NjE0NjU1Mg.Gdav9V.DoNVLt6CYLMFZs75f1msjQ63W_LkeEYx43t5Qk"
on_ready_message = "Bot está pronto como "
on_message_response = "Olá!"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f' {on_ready_message} {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('python'):
        await message.channel.send(on_message_response)

client.run(bot_token)