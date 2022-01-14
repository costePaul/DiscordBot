import discord
import re
import random
from discord.utils import get

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
    'Aurelien': ['aure', 'auré'],
    'hackerz': ['code', 'matrice', 'hack']
}
dico_normal_reacts = {
    '🕊️': ['bashing'],
    '❤️' : ['je t\'aime', 'keur', 'bro', 'bonne nuit', 'bn', 'les amis', 'les zamis']
}

######## Modération ##################

ban_words = ['marc serre', 'vlaminck', 'thomate', 'agent m', ':eye: :lips: :eye:', 'cringe', 'agent z', 'zemmour', 'corinne', 'agent c', 'z0zz', 'bérénice']
offset = 2 # number of last banWords not displayed
limit_ban_cachot = 2
people_to_watch = ['ArthurDo#6600', 'Jérémy Morlier#0866', 'aure_goose#5443']
corresponding_role = ['Son Lumières et Images', 'Connard des crepes', 'chef de projet BTP']
counter = [0]*len(people_to_watch)

######### Fonctions ###############

def search_for(liste_str, message):
    return any(bool(re.search(word, message.content.lower())) for word in liste_str)

########## Main class #############

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    ########## EDIT ##############
    async def on_message_edit(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        #ban words
        if search_for(ban_words, message):
            await message.delete()
            member = message.author
            with open('ASCyRespond/log.txt', 'a') as f:
                f.write(str(member)+' said :'+message.content+'\n')
            await message.channel.send('Le message précédent de '+str(member)+' enfreint les conditions d\'utilisation de ce serveur.')

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
            for index,people in enumerate(people_to_watch):
                if str(member)==people:
                    counter[index] += 1
                    if counter[index] == limit_ban_cachot:
                        counter[index] = 0
                        await member.remove_roles(get(member.guild.roles, name=corresponding_role[index]))
                        message.channel.send('L\'utilisateur'+str(member)+' a enfreint 1à fois (de plus ?) les conditions d\'utilisation de ce serveur, il a été mis au cachot. @Paul C#9115')

        #libere
        if search_for(['!libere', '!libère'],message):
            msg = str(message.content)[8:]
            for index,nom in enumerate(people_to_watch):
                if bool(re.search(nom, msg)):
                    member_name = get(message.guild.members, name=nom)
                    await member.add_roles(get(member_name.guild.roles, name=corresponding_role[index]))

        #ban words list
        if search_for(['!banwordslist'],message):
            await message.channel.send(str(ban_words[:-offset]))
        #ban count
        # if search_for(['!bancount'],message):
        #     await message.channel.send(str(ban_words[:-1]))
        
        ########### SENDING MSGs #######################
        
        #jeremy
        if search_for(['jérémy'], message):
            await message.channel.send('ça s\'écrit \'jérémie\'')
        #ski
        if search_for(['ascy','jérémy','jerem'], message):
            await message.channel.send(':skier:')
        #kenobi
        if search_for(['hello there'], message):
            await message.channel.send('General Kenobi')
            await message.channel.send(get(message.guild.emojis, name='faucon'))
        #combien
        if str(get(message.guild.emojis, name='COMBIEN')) in message.content:
            await message.reply(random.randint(1,100000000))

        ########## Edge case in reactions ############
        
        #palaref
        if search_for(['palaref'], message):
            await message.add_reaction(get(message.guild.emojis, name='GLAREF'))
            await message.add_reaction(get(message.guild.emojis, name='NotApproved'))
        #rapgod
        if len(message.content) >= 500:
            await message.add_reaction(get(message.guild.emojis, name='rapgod'))
        
        ############# YT LINKS #################
        
        #parti communiste
        if search_for(['parti communiste'], message):
            await message.channel.send('https://www.youtube.com/watch?v=mXWtt-rn49k')
        #tu as recu les photo
        if search_for(['tu as recu les photos'], message):
            await message.channel.send('https://www.youtube.com/watch?v=aZyEXv9nRNE')

        #############  REACTS #################
        for key,value in dico_customz_reaction.items():
            if search_for(value, message):
                await message.add_reaction(get(message.guild.emojis, name=key))
                
        for key,value in dico_normal_reacts.items():
            if search_for(value, message):
                await message.add_reaction(key)

client = MyClient()
client.run(TOKEN)