import asyncio, discord ,setting
from activity_log import log_actvity, log_start_actvity



client = discord.Client()
app = discord.Client()
Setting = setting.Settings()

@client.event
async def on_ready():
     print("Finsh login" % ())
     await client.change_presence(game=discord.Game(name="MK help", type=0))



@client.event
async def on_message(message):
                if "MK notice " in message.content:
                    if message.author.id == Setting.owner_id:
                        # DPNK 사용 구문 시점
                        embed=discord.Embed(title="MK BOT all notice system", color=0xb2ebf4)
                        embed.add_field(name="Send Notice is readying!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        mssg = await client.send_message(message.channel, embed=embed)
                        a = []
                        b = []
                        e = []
                        ec = {}
                        embed=discord.Embed(title="MK BOT all notice system", color=0xb2ebf4)
                        embed.add_field(name="I'm send all servers notice!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        await client.edit_message(mssg, embed=embed)
                        for server in client.servers:
                            for channel in server.channels:
                                for tag in ["notice", "공지", "알림", "Alarm"]:
                                    if tag in channel.name:
                                        dtat = True
                                        for distag in ["밴", "경고", "제재", "길드", "ban", "worry", "warn", "guild"]:
                                            if distag in channel.name:
                                                dtat = False
                                        if dtat:
                                            if not server.id in a:
                                                try:
                                                    await client.send_message(channel, message.content)
                                                except discord.HTTPException:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "HTTPException"
                                                except app.Forbidden:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "Forbidden"
                                                except app.NotFound:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "NotFound"
                                                except discord.InvalidArgument:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "InvalidArgument"
                                                else:
                                                    a.append(str(server.id))
                                                    b.append(str(channel.id))
                        asdf = "```\n"
                        for server in client.servers:
                            if not server.id in a:
                                try:
                                    ch = await client.create_channel(server, "MK-BOT-notice")
                                    await client.send_message(ch, "An announcement channel could not be found, resulting in channel creation. Please get DM. `컴퓨터의모든팁들#6225`")
                                    await client.send_message(ch, message.content)
                                except:
                                    asdf = asdf + str(server.name) + "[Channel creation failed.]\n"
                                else:
                                    asdf = asdf + str(server.name) + "[Channel generation and retransmission successful.]\n"
                        asdf = asdf + "```"
                        embed=discord.Embed(title="MK BOT all notice system", color=0xb2ebf4)
                        embed.add_field(name="Send to all channel, it was finsh!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        bs = "```\n"
                        es = "```\n"
                        for bf in b:
                            bn = client.get_channel(bf).name
                            bs = bs + str(bn) + "\n"
                        for ef in e:
                            en = client.get_channel(ef).name
                            es = es + str(client.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
                        bs = bs + "```"
                        es = es + "```"
                        if bs == "``````":
                            bs = "``` ```"
                        if es == "``````":
                            es = "``` ```"
                        if asdf == "``````":
                            asdf = "``` ```"
                        sucess = bs
                        missing = es
                        notfound = asdf
                        embed.add_field(name="The following channels succeeded in sending the announcement :", value=sucess, inline=False)
                        embed.add_field(name="The following channels failed to send notifications :", value=missing, inline=False)
                        embed.add_field(name="Servers with no keywords found include :", value=notfound, inline=False)
                        await client.edit_message(mssg, embed=embed)
                        # DPNK 사용 구문 종점
                        log_actvity("I send Notice for all Server. (content : %s\nSuccess : %s\nFail : %s\nNotfound : %s)." % (message.content, sucess, missing, notfound))
    
     
                if "MK finsh working" == message.content:
                    if message.author.id == Setting.owner_id:
                        await client.send_message(message.channel, "<@%s>, Stops the bot. Offline within 5 minutes (Discord API Delay)." % (message.author.id))
                        await client.change_presence(game=discord.Game(name="Offline", type=0))
                        log_actvity("Change status to offline (Request by. %s)." % (message.author.id))
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

    
client.run('NTI2MjM5MjE2NzQ1NzA5NTY4.DyQ-aQ.TBybWBU9knY_MhLOVVEa-ezbmrU')    
