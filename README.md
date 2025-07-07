# discord_ban
Useful tools for banning users on Discord

### Usage

- If you don't have a dev app yet, create one on https://discord.com/developers/applications/.
- Create a bot for your app. Save its token for later.
- Grant priviliged gateway intents to your newly made bot (just tick the options).
- Invite the bot on your server, with appropriate permissions (namely, read and ban).

Next :
- If you don't have it yet, install [python](https://www.python.org/downloads/).
- Install discord.py via pip ([guide here](https://discordpy.readthedocs.io/en/stable/intro.html)).

Then, in autoban.py, removing the <> :
- Replace '<your_bot_token_here>' with your bot's private token.

Finally, run ban_pseudo.py inside your terminal of choice.
The bot will only work while the script is running.
