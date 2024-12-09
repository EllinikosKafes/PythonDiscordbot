# Bot commands
# Author Matheus Aires - Kaazeeb

from discord.ext import commands
from blackjack import *

current_games = dict()

def setup_commands(bot: commands.Bot):
    @bot.command(name='help')
    async def call_help(ctx):
        message = help()
        await ctx.send(message)

    @bot.command(name='play')
    async def call_play(ctx):
        message = play(ctx)
        await ctx.send(message)
    
    @bot.command()
    async def test_cards(ctx):
        card_art = Card.print((10, 28), True)
        await ctx.send(f"```{card_art}```")

def help():
    message = (
        "```ini\n"
        "[help]    List of commands.\n"
        "[play]    Start a game.\n"
        "[current] To ask about the state of a current gaming session.\n"
        "[remind]  To see the current state of a game if in the middle of one.\n"
        "[quit]    To end a gaming session.\n"
        "```"
    )
    return f"{message}"


def play(ctx):
    if ctx.author in current_games:
        message = (
            f"{ctx.author}, it appears you already in a game!\n"
            'If you would like to start a new game, quit the previous by using "$quit".\n'
            'If you would like to inquire about the state of your current game say "$current".'
        )
        return message

    current_games[ctx.author] = Session()

    message = (
        f"Let's play a game, {ctx.author}.\n"
        'At any stage, if you would like to hear the commands, just say "$help".'
    )
    return message
