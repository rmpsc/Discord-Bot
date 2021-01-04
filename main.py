import discord
import random
import os  # allows access into .env files
from discord.ext import commands, tasks
from keep_alive import keep_alive

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

# random statuses
stat = [discord.Status.online, discord.Status.idle, discord.Status.dnd]

# random activities
act = [discord.Game('Gridshot'), discord.Game('myself :/'),
    discord.Game('Tik Tak Toe'), discord.Game('BEYBLADE'), discord.Game('Yu-Gi-Oh!'),
    discord.Game('Pokémon GO'), discord.Game('Pocket God'),
    discord.Game('coolmathgames.com'), discord.Game('Search and Destroy in Terminal'),
    discord.Activity(type=discord.ActivityType.listening, name='Ram Ranch'),
    discord.Activity(type=discord.ActivityType.listening, name='NIKI'),
    discord.Activity(type=discord.ActivityType.listening, name='Joji'),
    discord.Activity(type=discord.ActivityType.listening, name='Ginuwine'),
    discord.Activity(type=discord.ActivityType.listening, name='Take Care'),
    discord.Activity(type=discord.ActivityType.watching, name='TenZ'),
    discord.Activity(type=discord.ActivityType.watching, name='Game of Thrones'),
    discord.Activity(type=discord.ActivityType.watching, name='HIMYM'),
    discord.Activity(type=discord.ActivityType.watching, name='Rick and Morty')]


# TASKS
@tasks.loop(hours=1)
async def change_status():
    await bot.change_presence(status=random.choice(stat), activity=random.choice(act))


# EVENTS
@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user.name} is all set')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(721275182752464919)
    await channel.send(f'**{member.name}** is now a sweat! welcome <:hot_face:795781546047963187> <:sweat_drops:795781585789911040>')


@bot.event
async def on_message(message):
    if message.author.bot:
        return
        
    if '10 man' in message.content:
        await message.channel.send('<:billed_cap:793982003820101662>')
    
 
    # allows commands to be called async
    await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 793644726170681364:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            
            if member is not None:
                await member.add_roles(role)
                print(f'{role} role added to {member}')
            else:
                print('member not found')
        else:
            print('role not found')


@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 793644726170681364:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            # payload.member only works when adding a role
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print(f'{role} role removed from {member}')
            else:
                print('member not found')
        else:
            print('role not found')


# catches general errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist boi')


# COMMANDS
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()  # returns the ping of the user
async def ping(ctx):
    await ctx.send(f'<:ping_pong:793995689825665035>pong! {round(bot.latency * 1000)}ms')


@bot.command()  # returns the minecraft server name
async def mcserver(ctx):
    await ctx.send('MINECRAFT SERVER <:MINECRAFT:793628933123211264>\nmc.bighatchet.com:7357')


@bot.command()
@commands.has_permissions(manage_messages=True)  # check which limits which users can call this command
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount + 1)


# includes all the cogs/classes in program
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


keep_alive()  # keeps bot running
bot.run(os.getenv('token'))  # uses bots token to begin running
