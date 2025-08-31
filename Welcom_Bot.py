import discord

TOKEN = "自分のBotTOKENをここに張り付ける。"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

CHANNEL_ID = 1411725186981691404

@client.event
async def on_member_join(member):
    channel = client.get_channel(CHANNEL_ID)
    if channel is not None:
        await channel.send(f'ようこそ！！ {member.mention}!')
    else:
        print(f'チャンネルが見つかりませんでした')

#ボットの起動
client.run(TOKEN)