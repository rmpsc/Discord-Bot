import discord
import requests
import random
from discord.ext import commands

class Simba(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("shibashiba is online")
        

    # Commands
    @commands.command()
    async def shiba(self, ctx):
        url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
        response = requests.get(url)
        shiba = response.json()
        await ctx.send('**BORKBORK**')
        await ctx.send(shiba[0])

# sets up cog
def setup(client):
    client.add_cog(Simba(client))