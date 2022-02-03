First attempt at a discord bot stemming from a running joke on a server.
Mostly reacts or answers with customed emojiis.

## Setup

Clone the repo

```
git clone https://github.com/costePaul/DiscordBot.git
```

Créer un venv...
```
python3 -m venv env
```
...et l'activer
```
source ./env/bin/activate
```
Download the discord library
```
pip install discord
```
Download other libraries
```
pip install beautifulsoup4
pip install feedparser
```
The bot's token will also be needed in a txt file (token.txt) in the ASCyRespond folder in order to link the script to the bot.

The file `install_certifi.py` can be run to resolve issues with accepting Discord certificate to establish connexion.
