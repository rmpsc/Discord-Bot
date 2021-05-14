import discord
import random
from discord.ext import commands

class Val(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('val is online')

    # Commands
    @commands.command()
    async def acai(self, ctx):
        await ctx.send('If acai has a million number of fans i am one of them . if acai has ten fans i am one of them . if acai has only one fan that fan is me . if acai has no fans, that means i am no more on the earth . if the world is against acai , i am against the world. i love #acai till my last breath.. .. Die Hard fan of acai . Hit Like If you Think acai is the Best player & Smartest In the world')


    @commands.command()
    async def agent(self, ctx):
        agents = ['pick jett wdym <:tenz:760654681272877116>', 'brim baby', 'breach lol', 'gib me a corpse', 'omen diff', 'JOKE SOVA YA DED', 'bomb buddy out', 'ysas main', 'YOUR DUTY IS NOT OVAH', 'shak dart', 'snake ass foo', 'zoo keeper', 'kevin nguyen', 'michonne']
        await ctx.send(random.choice(agents))

# sets up cog
def setup(client):
    client.add_cog(Val(client))
    