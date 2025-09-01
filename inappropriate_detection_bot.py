import discord

TOKEN = "YOUR_TOKEN"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

inappropriate_member = []
inappropriate_count = []


@client.event
async def on_message(message):
    #今はボットに返信してもらうためコメントアウト
    # if message.author == client.user:
    #     return

    if "不適切" in message.content:  # ここに検出したい不適切な言葉を追加
        await message.channel.send(f'{message.author.mention} さん、不適切な言葉は控えてください。')

        if message.author not in inappropriate_member:
            inappropriate_member.append(message.author)
            inappropriate_count.append(1)
        else:
            index = inappropriate_member.index(message.author)
            inappropriate_count[index] += 1
        
        if inappropriate_count[index] >= 3:  # 3回以上不適切な言葉を使った場合
            await message.channel.send(f'{message.author.mention} さん、3回以上不適切な言葉を使用したため、退場処分とします。')
            await message.author.kick(reason="不適切な言葉を使用したため")

#ボットの起動
client.run(TOKEN)