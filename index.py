import discord
INTENTS = discord.Intents.all()
client = discord.Client(intents = INTENTS)
# Discord 클라이언트 객체 생성

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
# 봇이 메시지를 받았을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):
    # 메시지를 보낸 사람이 봇 자신이면 무시
    if message.author == client.user:
        return

    if message.content.startswith('!밥'):
        await message.channel.send('옴뇸뇸뇸뇸')

    if message.content.startswith('!몸무게'):
        await message.channel.send('81.3그람!!')

    if message.content.startswith('!절미'):
        await message.channel.send('찍찍!')
    
    activity = discord.Game(name="해바라기 씨앗 먹기")
    await client.change_presence(activity=activity)

client.run('MTI3NzE4NTI5NjE0ODIwNTY1OA.G18tVo.JIcQ3bbtmA8IG3kRt4IEp5VK0nUqC4eqpEdX9I')