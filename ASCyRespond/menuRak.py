import feedparser
import bs4
from datetime import date
import calendar

def menu_RAK() :
    curr_date = date.today()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    frenchDays = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    todayIndex = days.index(calendar.day_name[curr_date.weekday()])
    today = frenchDays[todayIndex]

    rakFeed = feedparser.parse("http://services.imt-atlantique.fr/rak/rss/menus.xml")
    entry = rakFeed.entries[1]
    html_doc = entry.description
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    plats = []
    debutPlat = False
    for balise in soup :
        if (todayIndex < 5) and (balise.string == frenchDays[todayIndex + 1]) :
            debutPlat = False  

    if debutPlat :
        if balise.name == 'a' :
            plats.append(balise.string)
        if balise.name == 'strong' :
            plats.append("\n" + balise.string + "\n")

    if balise.string == today :
        debutPlat = True
    message = today + " : " + str(curr_date.day) + "/" + str(curr_date.month) + "/" +\
         str(curr_date.year) + "\n" + "Menu du jour : \n"
    for plat in plats :
        message += plat + "\n"
    return message