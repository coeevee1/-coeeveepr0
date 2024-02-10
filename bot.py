import discord
from discord import app_commands
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await tree.sync()

@tree.command(name='coeevee', description='')
async def coeeveecmd(interaction: discord.Interaction, meesge: str):

    client.run('MTIwNTU5NDA1OTgwOTIyNjc1Mg.G70MNE.aIm5a_J2uqvEyZc4UEkAh-AetQWAo6Fx_c_uVk')

