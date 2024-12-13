# Bot commands
# Author Matheus Aires - Kaazeeb

from discord.ext import commands
from utils.session import Session

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

    @bot.command(name='quit')
    async def call_quit(ctx):
        message = quit(ctx)
        await ctx.send(message)

    @bot.command(name='deal')
    async def call_deal(ctx):
        message = deal(ctx)
        await ctx.send(message)
    

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
            "```"
            f"{ctx.author}, it appears you already in a game!\n"
            'If you would like to start a new game, quit the previous by using "$quit".\n'
            'If you would like to inquire about the state of your current game say "$current".'
            "```"
        )
        return message

    current_games[ctx.author] = Session()

    message = (
        "```"
        f"Let's play a game, {ctx.author}.\n"
        'At any stage, if you would like to hear the commands, just say "$help".'
        "```"
    )
    return message

def quit(ctx):
    if ctx.author not in current_games:
        message = (
            "```"
            "I have never seen you in my life.\n"
            "Get out of here!"
            "```"
        )
        return message
    
    session = current_games[ctx.author]

    message = (
        "```"
        f"We have played {session.games} games.\n"
        f"You won {session.score} of them. Good job!"
        "```"
    )
    current_games.pop(ctx.author)
    return message

def deal(ctx):
    if ctx.author not in current_games:
        message = (
            "```"
            f"{ctx.author}, we are not currently playing!\n"
            'If you would like to start a game, say "$play".\n'
            "```"
        )
        return message
    
    s = current_games[ctx.author]

    if s.game.state:
        message = (
            "```"
            "You already have your cards!\n"
            "If you would like to see the current state of the game "
            'say "$remind".\n'
            "```"
        )
        return message

    return s.game.deal()
    
