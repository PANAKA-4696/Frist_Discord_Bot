import discord

#ボットトークンを指定(Discord Developer Portalから取得)
TOKEN = "自分のBotTOKENをここに張り付ける。"

#Discordクライアントを作成
client = discord.Client(intents=discord.Intents.all())

#ボットが起動したときに実行するイベントハンドラ
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#メッセージを受け取ったときに実行するイベントハンドラ
@client.event
async def on_message(message):
    #メッセージを送信したユーザーがボットでないことを確認
    if message.author == client.user:
        return
    
    #メッセージが"hello"だった場合、"hay"と返信
    if message.content == "hello":
        await message.channel.send("hay")
    elif message.content == "goodnight":
        await message.channel.send("bye")

#ボットを起動
client.run(TOKEN)