@bot.event
async def on_ready():
  while True:
    channel = bot.get_channel(ID)   # Channel ID (Voice Channel)
    guild = bot.get_guild(ID) # Server ID / Guild ID
    await channel.edit(name=f'Members: {len(guild.members)}')
    await asyncio.sleep(300)