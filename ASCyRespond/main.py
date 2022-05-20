import discord
import re
import random
from discord.utils import get
from menuRak import menu_RAK

# to add the bot to a server
LINK = 'https://discord.com/api/oauth2/authorize?client_id=919215340020432936&permissions=534723950656&scope=bot'
# used by the script to specify which bot to control
with open('./ASCyRespond/token.txt', 'r') as f:
    TOKEN = f.read()


############ Reacts database ###############

dico_customz_reaction = { # emoji_str : list_of str triggers 
    'faucon': ['faucon'],
    'honteux': ['honteux'],
    'GLAREF': ['la ref'],
    'BDD': ['bdd'],
    'PALU': ['la doc'],
    'nantais': ['nantais', 'nantes'],
    'IMFAT': ['imsat','imfat'],
    'OurSolution': ['notre', 'commu'],
    'zrtLogo': ['zera'],
    'MV': ['mv','mistermv', 'plan q'],
    'Aurelien': ['aurelien', 'auré'],
    'hackerz': ['code', 'matrice', 'hack'],
    'seemsgood': ['jérémie']
}
dico_normal_reacts = {
    '🕊️': ['bashing'],
    '❤️' : ['je t\'aime', 'keur', 'bro', 'bonne nuit', 'bn', 'les amis', 'les zamis']
}

######## Modération ##################

ban_words = ['marc serre', 'vlaminck', 'thomate', 'agent m', ':eye::lips::eye:', 'cringe', 'agent z', 'zemmour', 'corinne', 'agent c', 'z0zz', 'bérénice']
offset = 2 # number of last banWords not displayed

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
        
        ########## Modération ##############
        #ban words
        if search_for(ban_words, message):
            await message.delete()
            member = message.author
            with open('ASCyRespond/log.txt', 'a') as f:
                f.write(str(member)+' said :'+message.content+'\n')
            await message.channel.send('Le message précédent de '+str(member)+' enfreint les conditions d\'utilisation de ce serveur.')
        #ban words list
        if search_for(['!banwordslist'],message):
            await message.channel.send(str(ban_words[:-offset]))
        
        ########### SENDING MSGs #######################
        
        #jeremy
        liste_chara = ['jérémy','jerem', 'jérem', 'jerém']
        if search_for(liste_chara, message):
            await message.channel.send('ça s\'écrit \'jérémie\'')
        #ski
        liste_chara = ['ascy']
        if search_for(liste_chara, message):
            await message.channel.send(':skier:')
        #kenobi
        liste_chara = ['hello there']
        if search_for(liste_chara, message):
            await message.channel.send('General Kenobi')
            await message.channel.send(get(message.guild.emojis, name='faucon'))
        #combien
        if str(get(message.guild.emojis, name='COMBIEN')) in message.content:
            await message.reply(random.randint(1,100000000))
        #rak
        liste_chara = ['!rak', '!menu', 'j\'ai faim']
        if search_for(liste_chara, message):
            await message.channel.send(menu_RAK())
        liste_chara = ['!lienrak']
        if search_for(liste_chara, message):
            await message.reply('http://services.imt-atlantique.fr/rak/')

        ########## Edge case in reactions ############
        
        #palaref
        liste_chara = ['palaref']
        if search_for(liste_chara, message):
            await message.add_reaction(get(message.guild.emojis, name='GLAREF'))
            await message.add_reaction(get(message.guild.emojis, name='NotApproved'))
        #rapgod
        if len(message.content) >= 500:
            await message.add_reaction(get(message.guild.emojis, name='rapgod'))
        
        ############# YT LINKS #################
        
        #parti communiste
        liste_chara = ['parti communiste']
        if search_for(liste_chara, message):
            await message.channel.send('https://www.youtube.com/watch?v=mXWtt-rn49k')
        #tu as recu les photo
        liste_chara =['tu as reçu les photos','tu as recu les photos']
        if search_for(liste_chara, message):
            await message.channel.send('https://www.youtube.com/watch?v=aZyEXv9nRNE')

        liste_chara =['j\'ai faim']
        if search_for(liste_chara, message):
            await message.channel.send('https://www.youtube.com/watch?v=9JB2FK38CaY')

        liste_chara =['g@m3rz']
        if search_for(liste_chara, message):
            await message.channel.send('https://www.youtube.com/watch?v=5jqRg90ApdM')

        liste_chara =['oskour']
        if search_for(liste_chara, message):
            await message.channel.send('https://www.youtube.com/watch?v=V2ZkgEAhRUY')

        #############  REACTS #################
        for key,value in dico_customz_reaction.items():
            if search_for(value, message):
                await message.add_reaction(get(message.guild.emojis, name=key))
                
        for key,value in dico_normal_reacts.items():
            if search_for(value, message):
                await message.add_reaction(key)

client = MyClient()
client.run(TOKEN)
