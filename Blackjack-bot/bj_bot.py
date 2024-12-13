# Implements a blackjack bot game for discord
# Author Matheus Aires - Kaazeeb
# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from bj_commands import setup_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)
setup_commands(bot)

if __name__ == '__main__':
    with open('secret.txt', 'r') as f:
        token = f.readline()

    bot.run(token)