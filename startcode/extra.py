import main

laatste_2_berichten = []
async for i in message.channel.history(limit=2):
   laatste_2_berichten.append(i)

@bot.event
async def setup_hook():
    await bot.tree.sync()
    print(f"Slash commando's gesynchroniseerd.")


@bot.hybrid_comm(name = "test", with_app_command = True, description = "Testing mijn test command")

