import discord
from discord.ext import commands

TOKEN = 'NzQzMDgzNTIxMDA1OTc3NjUw.XzPgdQ.tNNwPCbl1SlUjKUU_7lZhYh21UY'
BOT_PREFIX = '\''

# Do not touch this!  
client = commands.Bot(command_prefix=BOT_PREFIX)

# Bot setup.
@client.event
async def on_ready():
    # Prints 'Bot is ready' when bot is online and ready to use.
    print('Bot is online.')


# if typing a wrong command, if it will not be here it will throw an error in the console, and you don't want this.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Didn't find a command with that name, type `{BOT_PREFIX}help` for a list of commands. \u274c")


# ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Good Morning
@client.on_messege():




# Token of the bot, Do not touch!
client.run(TOKEN)