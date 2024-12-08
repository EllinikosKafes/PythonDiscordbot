# Bot commands
# Author Matheus Aires - Kaazeeb

from discord.ext import commands
from blackjack import Card

def setup_commands(bot: commands.Bot):
    @bot.command()
    async def play(ctx):
        await ctx.send(f"Let's play a game, {ctx.author}.")
    
    @bot.command()
    async def test_cards(ctx):
        card_art = Card.print((10, 28), True)
        await ctx.send(f"```{card_art}```")

