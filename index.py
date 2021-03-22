from discord import TextChannel
from discord.ext.commands import Bot, Context
from json import load

with open("config.json") as f:
    config = load(f)

bot = Bot(command_prefix=config["prefix"])

@bot.event
async def on_ready():
    async for guild in bot.fetch_guilds(limit=None):
        #Fetches all guilds
        print(guild.name)

@bot.command(aliases=["spam", "sm", "cs", "rape", "crape", "cr"])
async def _webhook_channel_spammer(ctx:Context, arg:str=None):
    """Proof of concept of webhook/channel spammer in just one line!
    Equivelant to: ```py
    for channel in ctx.guild.channels:
        if type(channel) == TextChannel:
            for channel in await channel.webhooks():
                channel.send(arg or config.get("raid_message"))
    ```
    More of a WIP thing since it is kind of slow, but you get the point!
    """
    [
        await channel.send(arg or config.get("raid_message")) for channel in ctx.guild.channels if type(channel) == TextChannel for channel in await channel.webhooks()
    ]

bot.run(config.get("token"))
