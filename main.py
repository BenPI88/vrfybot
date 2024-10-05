import discord, asyncio
client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree

@client.event
async def on_join(guild):
    try
    for i in guild.channels