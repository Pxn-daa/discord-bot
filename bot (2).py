import discord
from discord.ext import commands
from discord.ext.commands import errors
from datetime import datetime
import requests
import time
from keep_alive import keep_alive
import json
import random
import asyncio
import time
import colorama
import aiohttp
import glob, os, os.path
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')


@bot.event
async def on_ready():
  print('ꜱᴛᴇᴀʟᴛʜ | Bot Has Been Started')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{len(bot.guilds)} Servers | $help"))

@bot.command()
async def help(ctx):

  help = discord.Embed()
  help.set_author(name='Available Commands ↴', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
  help.set_thumbnail (url='https://cdn.discordapp.com/avatars/611756007152156703/a_50c2fcccaffd046b2e330216ae7942c3.gif?size=256&f=.gif')
  help.add_field(
        name='\nㅤ\ntools | **shows tool commands**\nfun | **shows fun commands**\nmod | **shows mod commands**\nsupport | **.support**', value='ㅤ', inline=False)
  
  help.timestamp = datetime.now()

  await ctx.send(embed=help)
    
@bot.command()
async def fun(ctx):
    fun = discord.Embed()
    fun = discord.Embed()
    fun.set_author(name='Available Commands ↴', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    fun.set_thumbnail (url='https://cdn.discordapp.com/avatars/611756007152156703/a_50c2fcccaffd046b2e330216ae7942c3.gif?size=256&f=.gif')
    fun.add_field(
        name='\nㅤ\nmeme | **Random Meme**\n8ball | **Answers Truthly**\npenis | **Penis Size**\n1337 | **Hacker Talk**\nslot | **Slot Machine**\nyon | **Yes Or No**', value='ㅤ', inline=False)
    
    fun.timestamp = datetime.now()

    await ctx.send(embed=fun)
  
@bot.command()
async def tools(ctx):
    tools = discord.Embed()
    tools.set_author(name='Available Commands ↴', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    tools.set_thumbnail (url='https://cdn.discordapp.com/avatars/611756007152156703/a_50c2fcccaffd046b2e330216ae7942c3.gif?size=256&f=.gif')
    tools.add_field(
        name='\nㅤ\nnmap | **Basic Nmap Scan**\nping | **Pings An IP**\nresolve | **Resolve An IP**\nhostsearch | **DNS Records**', value='ㅤ', inline=False)

    tools.timestamp = datetime.now()

    await ctx.send(embed=tools)
              
  
  
@bot.command()
async def mod(ctx):
  
  mod = discord.Embed()
  mod.set_author(name='Status : Online', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
  mod.set_thumbnail (url='https://cdn.discordapp.com/avatars/611756007152156703/a_50c2fcccaffd046b2e330216ae7942c3.gif?size=256&f=.gif')
  mod.add_field(name='Available Commands ↴', value='***mute*** | mutes a user\n***unmute*** | unmutes a user\n***kick*** | kicks a user\n***ban*** | bans a user\n***whois*** | users information\n***clear*** | clears chat\n***roleinfo*** | role information\n***mc*** | member count\n***warn*** | warns a user\n***warnings*** | users warnings\n***clearwarns*** | clears warnings',inline = False)
  
  
   
  mod.timestamp = datetime.now()
  await ctx.send(embed=mod)

  
@bot.command()
async def meme(ctx):
    response = requests.get(url="https://meme-api.herokuapp.com/gimme")
    j = json.loads(response.text)
    meme = discord.Embed(title=f"{j['title']}", color=16)
    meme.set_image(url=j['url'])
    meme.timestamp = datetime.now()
    await ctx.send(embed=meme)


@bot.command()
async def nmap(ctx, ip):
	response = requests.get(f'https://api.hackertarget.com/nmap/?q={ip}')

	nmap = discord.Embed(
	    title='Nmap Scan ↴', color=16, description=f'{response.text}')
	nmap.timestamp = datetime.now()
	await ctx.send(embed=nmap)


@bot.command()
async def hostsearch(ctx, ip):
	response = requests.get(f'https://api.hackertarget.com/hostsearch/?q={ip}')

	hostsearch = discord.Embed(
	    title='Host Search ↴', color=16, description=f'{response.text}')
	hostsearch.timestamp = datetime.now()
	await ctx.send(embed=hostsearch)

@bot.command()
async def ping(ctx, ip):
	response = requests.get(f'https://api.hackertarget.com/nping/?q={ip}')

	ping = discord.Embed(
	    title='Host Status ↴', color=16, description=f'{response.text}')
	ping.timestamp = datetime.now()
	await ctx.send(embed=ping)

@bot.command()
async def resolve(ctx, ip):
	response = requests.get(f'https://api.apithis.net/host2ip.php?hostname={ip}')

	resolve = discord.Embed(
	    title='Resolving Host to IP ↴', color=16, description=f'{response.text}')
	resolve.timestamp = datetime.now()
	await ctx.send(embed=resolve)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked Bye Bye")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned Lol")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")        

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    membersRole = discord.utils.get(ctx.guild.roles, name="Members")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        membersRole = discord.utils.get(ctx.guild.roles, name="Members")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await member.remove_roles(membersRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    membersRole = discord.utils.get(ctx.guild.roles, name="Members")
    await member.remove_roles(mutedRole)
    await member.add_roles(membersRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
    await ctx.send(f'Q: {question}\nA: {random.choice(responses)}')
    
    
@bot.command()
async def yon(ctx, *, question):
 answers = ['yes', 'no']
 await ctx.send(f'Q: {question}\nA: {random.choice(answers)} ')
 
@bot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    color = 16
    
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=color)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)
    
   
@bot.command(aliases=['slots', 'bet'])
async def slot(ctx): 
 emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
 a = random.choice(emojis)
 b = random.choice(emojis)
 c = random.choice(emojis)
 slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
 if (a == b == c):
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
 elif (a == b) or (a == c) or (b == c):
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
 else:
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"})) 
     
    
@bot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)


    
@bot.command(name='invite', aliases=['inv'])
async def invite(ctx):
    invite = discord.Embed(title='Add Me To Your Server', color=16)
    invite.add_field(
      name='Click The Link Below', value='➥ https://discord.com/oauth2/authorize?client_id=765842610136809482&scope=bot&permissions=8', inline=False)
    invite.timestamp = datetime.now()
    await ctx.send(embed=invite)
    
@bot.command(name='support', aliases=['Support'])
async def support(ctx):
    support = discord.Embed(title='Support Server', color=16)
    support.add_field(
      name='Click The Link Below To Join', value='➥ https://discord.gg/aUAqpJx', inline=False)
    support.timestamp = datetime.now()
    await ctx.send(embed=support)
    
@bot.command(name='Credits', aliases=['creds'])
async def credits(ctx):
    support = discord.Embed(title='Credits ', color=16)
    support.add_field(
      name='These Are The Devs Of This Bot', value='➥ Lucidx#0001 and ꆛ҉P͓̽x͓̽n͓̽d͓̽a͓̽#9397', inline=False)
    support.timestamp = datetime.now()
    await ctx.send(embed=support)



@bot.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((000000)))

    await ctx.send(embed=b)
@bot.command()
@commands.has_permissions(ban_members=True)
async def warn(ctx, member: discord.Member = None, *, reason = None): # warns a member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=000000, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == ctx.message.author:
        e7 = discord.Embed(color=000000, description="Sorry, but you can't warn yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    if not os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        with open(f"{guild.id}-{member.id}-warns.txt", "w") as f10:
            f10.write("1")
            f10.close()
            e4 = discord.Embed(color=000000, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e4)
            if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=000000, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
            else:
                pass
            return
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "r")
        global warns
        warns = f.read()
        if warns == '0':
            f2 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f2.write('1')
            f2.close()
            e5 = discord.Embed(color=000000, description=f"{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!")
            e5.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e5)
            if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=000000, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
            else:
                pass
            return
        if warns == '1':
            f3 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f3.write('2')
            f3.close()
            e6 = discord.Embed(color=000000, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e6.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e6)
            if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=000000, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
            else:
                pass
            return
        if warns == '2':
            f4 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f4.write('0')
            f4.close()
            await member.ban(reason=reason)
            e9 = discord.Embed(color=000000, description=f"Looks like {member.mention} has been warned to often and now they're banned!")
            e9.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e9)
            if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=000000, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User banned (3 warns)')
                await log_channel.send(embed=e)
            else:
                pass
            return
@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to warn people")        



@bot.command()
@commands.has_permissions(ban_members=True)
async def clearwarns(ctx, member: discord.Member = None): # clears the warnings of a member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=000000, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "w")
        f.write('0')
        e9 = discord.Embed(color=000000, description=f"Successfully cleard the warnings of {member.mention}!")
        e9.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
        await ctx.send(embed=e9)
        if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=000000, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**)")
                e.set_author(name='Warns cleared')
                await log_channel.send(embed=e)
        else:
            pass
    else:
        await ctx.send('Looks like something went wrong...')

@clearwarns.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to clear warnings")        





@bot.command()
@commands.has_permissions(ban_members=True)
async def warnings(ctx, member: discord.Member = None): # shows the amount of warnings a member currently has
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=000000, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "r")
        warns = f.read()
        e3 = discord.Embed(color=000000, description=f'{member.mention} currently has **{warns}** warning(s)!')
        await ctx.send(embed=e3)
    else:
        await ctx.send('Looks like something went wrong...')

@warnings.error
async def warnings_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to view users warnings")        
        
@bot.command()
@commands.has_role('Staff')
async def clear(ctx, amount=200):
				await ctx.message.delete()
				await ctx.channel.purge(limit=amount)
				clear = discord.Embed(title='Cleared Chat ↴', color=16)
				await ctx.send(embed=clear)
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def pardon(ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
          user = ban_entry.banned_users

          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('Sorry you are not allowed to use this command.')
@bot.command(name='1337', aliases=['hacks'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')


@bot.command()
async def whois(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(
        
        timestamp=ctx.message.created_at,
        title=f"{member}'s Information ")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{member.id}")


    embed.add_field(
        name="Created Account On:",
        value=member.created_at.strftime("%a, %#d %B , %I:%M %p"))
    embed.add_field(
        name="Joined Server On:",
        value=member.joined_at.strftime("%a, %#d %B , %I:%M %p"))

    embed.add_field(
        name="\nRoles:", value="".join([role.mention for role in roles]),inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command(name='ownhelp', aliases=['modhelp'])
async def modhelp(ctx):
    support = discord.Embed()
    support.add_field(
      name='How To Setup', value='All Roles Apart From "Members" Must NOT Be Able To Talk\n"Muted" Role Must Not Have Any Perms', inline=False)
    support.timestamp = datetime.now()
    await ctx.send(embed=support)
   
keep_alive()
bot.run('NzU2NTk5NzA0MjM3NzY4NzQ1.X2UMYg.3pJJgMR2-oJCdptC-I8S8uhLyQw')
