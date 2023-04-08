import asyncio
import datetime
import discord
from discord.ext import commands
import re
import ct_ticket_tracker.db.queries
import ct_ticket_tracker.utils.bloons
from ct_ticket_tracker.exceptions import WrongChannelMention
from ct_ticket_tracker.classes import ErrorHandlerCog
from typing import Optional


class UtilsCog(ErrorHandlerCog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(name="longestround",
                                  description="Get the longest round and its duration for races.")
    @discord.app_commands.describe(end_round="The last round of the race.")
    async def longestround(self, interaction: discord.Interaction, end_round: int) -> None:
        round_lengths = [17.5, 19, 16.7, 17.3, 16.5, 18.7, 26.8, 28.866666666666667, 18.95, 47.983333333333334, 19.15,
                         17.383333333333333, 32.2, 26.616666666666667, 25, 16.016666666666666, 5, 26.816666666666666,
                         15.75, 5.233333333333333, 18.116666666666667, 8, 6.816666666666666, 9, 21.133333333333333,
                         14.5, 34.25, 5, 15.25, 13.066666666666666, 15.9, 27.95, 25.333333333333332, 36, 33.75,
                         20.983333333333334, 43.5, 29.05, 37.916666666666664, 1, 46.2, 11.6, 9.25, 23.666666666666668,
                         53.1, 7, 24.633333333333333, 55.71666666666667, 50, 28.966666666666665, 24.133333333333333,
                         20.55, 35, 19.4, 29.766666666666666, 16.166666666666668, 26.216666666666665, 43.98333333333333,
                         26.15, 1, 20, 48.28333333333333, 42.25, 9.516666666666667, 62, 22.75, 26.433333333333334,
                         8.433333333333334, 42.11666666666667, 41.13333333333333, 16.55, 21.683333333333334, 26.95,
                         82.38333333333334, 22.583333333333332, 1.7666666666666666, 58.916666666666664, 90, 60, 2,
                         26.466666666666665, 35.666666666666664, 60.2, 25, 10, 20.85, 10, 14.55, 20.733333333333334,
                         11.9, 30, 35, 20, 15, 50.8, 32.11666666666667, 5, 30, 12, 0.1
                         ]
        if end_round <= 0:
            await interaction.response.send_message(f"{end_round} is not a valid round.")
        longest = 0
        for game_round in range(min(100, end_round)):
            if round_lengths[longest] < round_lengths[game_round]:
                longest = game_round
        await interaction.response.send_message(f"The longest round is {longest+1} (lasts {round_lengths[round(longest)]}s).")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UtilsCog(bot))
