import discord

TOKEN = "YOUR_TOKEN"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "適切じゃない":
        await message.channel.send("不適切")

#ボットを起動
client.run(TOKEN)