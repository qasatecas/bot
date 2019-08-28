import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='**')

guildrs = []
rolesdict ={}

@bot.event
async def on_ready():
    print ("Здарова, шнырь")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + str(bot.user.id))
    

pizzaid = 301746183645298690
pizzaname = bot.get_guild(pizzaid)
namebot = 'welcome bot#8977'
xx = 100
players = {}
queue = {}
spisok = {}
nowp = {}
playersloop = {}
queueloop = []
duration = {}




@bot.event
async def on_raw_reaction_add(payload):
    
    
    guildid = payload.guild_id
    mesid = payload.message_id
    guild = bot.get_guild(guildid)
    userid = payload.user_id
    user = guild.get_member(userid)
    print(mesid)
    emoji = payload.emoji
    if mesid == 616312267067228195:
        if str(emoji) == '<:Villager_SSB4:492779328799768587>':
            await user.add_roles(guild.get_role(616232176035299345))
        elif str(emoji) == "<:csemoji:616253242350764042>":
            await user.add_roles(guild.get_role(616240053634727967))
        elif str(emoji) == "<:doraemoji:616253484454641684>":
            await user.add_roles(guild.get_role(616239956142063616))
        elif str(emoji) == "<:rainbowsixsiegelogologopngtransp:616253499822309376>":
            await user.add_roles(guild.get_role(616239912521564183))
        elif str(emoji) == "<:d2emoji:616253472228114432>":
            await user.add_roles(guild.get_role(616245379087859745))
        else:
            pass

@bot.event
async def on_raw_reaction_remove(payload):
    
    
    guildid = payload.guild_id
    mesid = payload.message_id
    guild = bot.get_guild(guildid)
    userid = payload.user_id
    user = guild.get_member(userid)
    
    emoji = payload.emoji
    if mesid == 616312267067228195:
        if str(emoji) == '<:Villager_SSB4:492779328799768587>':
            await user.remove_roles(guild.get_role(616232176035299345))
        elif str(emoji) == "<:csemoji:616253242350764042>":
            await user.remove_roles(guild.get_role(616240053634727967))
        elif str(emoji) == "<:doraemoji:616253484454641684>":
            await user.remove_roles(guild.get_role(616239956142063616))
        elif str(emoji) == "<:rainbowsixsiegelogologopngtransp:616253499822309376>":
            await user.remove_roles(guild.get_role(616239912521564183))
        elif str(emoji) == "<:d2emoji:616253472228114432>":
            await user.remove_roles(guild.get_role(616245379087859745))
        else:
            pass
    






bot.run("NjE2MjQyMzA1NDU1NjIwMTA5.XWbH1w.RJIf8x79zs-Tev3MvOLs1zaJjxI")
