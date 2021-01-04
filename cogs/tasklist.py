import discord
from discord.ext import commands
from replit import db


# idea: have a certain emoji for 10 man that adds them to the list
class Task_list(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('task_list is online')

    # Commands
    @commands.command(aliases = ['addt'])
    async def addtask(self, ctx, *, task):
        if 'task list' in db.keys():
            task_list = db['task list']
            task_list.append(task)
        else:
            db['task list'] = [task]

        await ctx.send(f'{task} added to task list!')

    @addtask.error
    async def addtask_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Make sure to use the correct format:\n>addt example_task')


    @commands.command(aliases = ['removet'])
    async def removetask(self, ctx, *, task):
        # makes sure the database already exists
        if 'task list' in db.keys():
            task_list = db['task list']
            if task in task_list:
                task_list.remove(task)
                db['task list'] = task_list
                await ctx.send(f'{task} removed!')
            else:
                await ctx.send(f'{task} does not exist!')
        else:
            await ctx.send(f'{task} does not exist!')


    @commands.command(aliases = ['cleart'])
    async def cleartasks(self, ctx):
        # makes sure the database already exists
        if 'task list' in db.keys():
            tasklist = db['task list']
            tasklist.clear()
            db['task list'] = tasklist  # updates tasklist
            await ctx.send('list is cleared!')
        else:
            await ctx.send('no list to clear!')


    @commands.command(aliases = ['showt', 'showtasks'])
    async def showtask(self, ctx):
        # makes sure the database already exists
        if 'task list' in db.keys():
            task_list = db['task list']
            await ctx.send('TASK LIST <:tenz:760654681272877116>')
            for task in task_list:
                await ctx.send(task)
        else:
            await ctx.send("there's no task_list to show")


# sets up cog
def setup(client):
    client.add_cog(Task_list(client))
    