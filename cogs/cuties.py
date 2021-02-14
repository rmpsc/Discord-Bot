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

    @commands.command()
    async def kitty(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search"
        header = {"x-api-key": "bab62365-5e13-46c1-8047-a0e9cfaa9299"}
        response = requests.get(url, header)
        kitty = response.json() # retrieves dictionary
        await ctx.send('**MEOWWW**')
        if len(kitty[0].get("breeds")) != 0:
            await ctx.send(kitty[0].get("breeds")[0].get("description"))
        await ctx.send(kitty[0].get("url"))


# sets up cog
def setup(client):
    client.add_cog(Simba(client))