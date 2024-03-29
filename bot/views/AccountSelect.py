import discord
from typing import Callable, Awaitable
import bloonspy


AccountChooserCallback = Callable[[discord.Interaction, bloonspy.btd6.User, str], Awaitable[None]]
AccountSelectorCallback = Callable[[discord.Interaction, str], Awaitable[None]]


class AccountSelect(discord.ui.Select):
    def __init__(self, users: list[tuple[bloonspy.btd6.User, str]], callback: AccountSelectorCallback = None):
        options = [
            discord.SelectOption(label=user.name)
            for user, _oak in users

        ]
        self.callback_func = callback
        super().__init__(
            placeholder="Select an account",
            options=options
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        if self.callback_func:
            await self.callback_func(interaction, self.values[0])


class AccountChooserView(discord.ui.View):
    def __init__(self,
                 users: list[tuple[bloonspy.btd6.User, str]],
                 callback: AccountChooserCallback,
                 timeout: float = 180):
        super().__init__(timeout=timeout)
        self.users = users
        self.callback = callback
        self.select = AccountSelect(users, callback=self.unverify_account)
        self.add_item(self.select)

    async def unverify_account(self, interaction: discord.Interaction, value: str) -> None:
        for user, oak in self.users:
            if user.name != value:
                continue
            await self.callback(interaction, user, oak)

