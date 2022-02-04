import discord
import re
from menuRak import menu_RAK

# to add the bot to a server
LINK = "https://discord.com/api/oauth2/authorize?client_id=939110583322705962&permissions=8&scope=bot"
# used by the script to specify which bot to control
with open('./RaKMenu/token.txt', 'r') as f:
    TOKEN = f.read()

######### Fonctions ###############

def search_for(liste_str, message):
    return any(bool(re.search(word, message.content.lower())) for word in liste_str)

########## Main class #############

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    ########### SEND ################    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        ########### SENDING MSGs #######################
        #rak
        liste_chara = ['!rak', '!menu', 'j\'ai faim']
        if search_for(liste_chara, message):
            await message.channel.send(menu_RAK())
        liste_chara = ['!lienrak']
        if search_for(liste_chara, message):
            await message.reply('http://services.imt-atlantique.fr/rak/')

client = MyClient()
client.run(TOKEN)
