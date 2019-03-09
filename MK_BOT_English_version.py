import asyncio, discord ,setting



client = discord.Client()
app = discord.Client()
Setting = setting.Settings()

@client.event
async def on_ready():
     print("Finsh login" % ())
     await client.change_presence(game=discord.Game(name="MK help", type=0))



@client.event
async def on_message(message):
                if "MK off" == message.content:
                    if message.author.id == Setting.owner_id:
                        await client.send_message(message.channel, "<@%s>, Stops the bot. Offline within 5 minutes (Discord API Delay)." % (message.author.id))
                        await client.change_presence(game=discord.Game(name="Offline", type=0))
                        quit() # 종료가성공적으로완료됌
                    else:
                        await client.send_message(message.channel, "<@%s>, You are not registered as a bot administrator." % (message.author.id))
     
                if message.content.startswith('MK bot profile'):
                  await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/518429267298877460/520534040269422612/2117d4628437cdf3.jpg")
                if message.content.startswith("MK minecraft site"):
                  await client.send_message(message.channel, "https://minecraft.net/ko-kr/?ref=m")
                if message.content.startswith('MK Hypixel'):
                  await client.send_message(message.channel, "Minecraft's largest server. Server Address : MC.hypixel.net") 
                if message.content.startswith("MK online"):
                  await client.send_message(message.channel, "I'm online!")  
                if message.content.startswith("MK invite link"):
                   await client.send_message(message.channel, "https://discordapp.com/api/oauth2/authorize?client_id=526239216745709568&permissions=0&scope=bot")
                if message.content.startswith('MK help'):
                   embed=discord.Embed()
                   embed.add_field(name='MK bot profile', value='Send a Bot profile photo.')
                   embed.add_field(name='MK minecraft site', value='I send minecraft site.')
                   embed.add_field(name='MK online', value='You can check a bot online.')
                   embed.add_field(name='MK help', value='MK BOT all commands you can see.')
                   embed.add_field(name='MK invite link', value='MK BOT invite link')
                   embed.add_field(name='MK BOT Developer and Helper', value='로봇폴린 부대표 아모 #4899 / 컴퓨터의모든팁들 #6225 / The_Adminator #4074 / 블맨 #5969')
                   await client.send_message(message.channel, embed=embed)
                if message.content.startswith('MK Korea version'):
                   embed=discord.Embed()
                   embed.add_field(name='MK BOT korea version invite', value='https://discordapp.com/oauth2/authorize?client_id=533202743532191747&scope=bot&permissions=124992')
                   embed.add_field(name='MK BOT korea version admin', value='컴퓨터의모든팁들#6225')
                   await client.send_message(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]             
client.run(access_token)    
