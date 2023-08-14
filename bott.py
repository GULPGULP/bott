import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    rainbow.start()

@tasks.loop(seconds=10)
async def rainbow():
    guild = bot.get_guild(1137731297347911742)

    role = discord.utils.get(guild.roles, name="Membres👥")

    if not role:
        role = await guild.create_role(name="Membres👥", color=discord.Color.default())
    
    colors = [discord.Color.red(), discord.Color.orange(), discord.Color.gold(), discord.Color.green(),
              discord.Color.blue(), discord.Color.purple()]
    
    for idx, color in enumerate(colors):
        await role.edit(color=color)
        await asyncio.sleep(10)  

bot.run('MTE0MDY0OTI2NTY1MjMxNDEzNA.Gt-q9X.ej_sB7vPAeqaLBRy8JRAfUeFpyj4tLa-PSXJK8')