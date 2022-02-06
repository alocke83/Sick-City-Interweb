#Sick City Interweb
#Adam Locke December 2021
#A text-based adventure side game for our cyberpunk RPG experience
#alocke1983@gmail.com

print('''\\\\
      \\\\\\\
      \\\\\\\
      PREPARING CONNECTION''')
import time
#so that I can make timed parts of the game.
import sys
import subprocess
#so that the game can install necessary modules
from datetime import date
print('\\\ ')
#this is used to select articles in the news service.
import csv
#in case I want to use csv files for data storage in order to provide persistence, modular game modes
print('|||diving past barriers\\\\\ ')
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymysql'])
import pymysql
print('|||penetrated barriers\\\\\ ')
#this exciting import lets me connect the game to my AWS RDS database so that I can offer dynamic experiences
import webbrowser
#i need this module so that the Vibe function can open the default browser for the user and get some youtube beats going for your hacking sesh

#||||||||||||||||||||||||||||||||||||||||||||||||||||||Operations Variables
endpoint='database-1.cirvmgmzswgg.us-east-2.rds.amazonaws.com'
userID='appUser'
Mpassword='4016coffee4011'
Tdatabase='none'
Tport=3306
articles=[]
articleLib={}

#||||||||||||||||||||||||||||||||||||||||||||||||||||||Structural Variables
user_heat=0 #user_heat measures how many illicit things you have done, when your heat maxes out the system will eject you
heat_limit=3 #the maximum heat you can accrue before being ejected
browse_history=[] #the browse history list is important so that the hack commands know how to behave based on where they were used from and other contextual things.  maybe scrutinizing it is a useful hack command, with maybe a command to hide your tracks.



#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||Function Definitions


#function to open the game and present the home screen
def home():
    global browse_history
    command_list=['email','news','shop','vibe','dragonPalace']
    print('####||||Sick City Interweb||||####\n\n')
    print('''Welcome to Sick City command line interweb, type commands to visit resources\n\n\n||||||||||Services\nemail\nnews\nvibe\nhowto\n\n||||||||||Commerce\nshop\ndragonPalace''')
    browse_history.append('home')
    comIn(command_list)

#function to tell how to play the game
def howTo():
    command_list=['home']
    print('''|||||||||||||||||||||||||||How to Play:\n
          The game is played from the python shell, you play by typing commands.  You don't have to use correct python syntax, each function has a plain word alias.\n\n
          On each screen there are commands on a list, you can type type the commands to perform the action.\n\n
          On some screens, you can use hidden commands that are only revealed during our live play sessions, like the password to someone's email.\n\n
          There are secret hacking commands that can be used from some screens as well, learning a secrety hacking word is done in our live sessions.\n\n
          There are portions of the game where you will be timed, if you don't type the commands fast enough, you'll be ejected from the system you got into.\n\n
          You can try the command \'home\' in order to return to the home screen.''')
    browse_history.append('howto')
    comIn(command_list)

#function to handle the command input
def comIn(alist):
    command_list = alist
    print('||||||Command\n')
    command=input()
    command_lib={'home':home,'email':email,'news':news,'vibe':vibe,'shop':shop,'dragonPalace':dragonPalace,'outrun':outrun,'vaporwave':vaporwave,'greenhouse':greenhouse,'sanic':sanic,'hack':hack,'request':request,'articles':articles}
    if command in command_list:                    #i am getting undefined error and it is very very defined by the time this function is called, i name the global within the function but still getting an undefined error when i try to call the dictionary variable; if i move the dictionary into the function i get a recursion error because as it loads the dictionary it executes each function, so that the home function goes into an infinite loop.
        command_lib.get(command)()
    else:
        print('||||||Invalid')
        comIn(command_list)
          

#function to handle the email messages
def email():
    command_list=['home']
    print('minigame not yet implemented, please return to home')
    comIn(command_list)


#functions to handle the news website
def news():
    command_list=['home','articles']
    print('|||||NSXS City News|||||\n\nWelcome to New Seattle Municipal News Desk, your source for current events.\nARTICLES\nHOME')
    comIn(command_list)
#this one pulls the news data from the database in order to provide articles
def get_news():
    conn=pymysql.connect(
    host=endpoint,
    user=userID,
    password=Mpassword
    )
    today=date.today()
    #today=str(today)
    #print(today)
    cur=conn.cursor()
    target='use appsDb'
    cur.execute(target)
    statement = 'select * from News'
    #print(statement)
    cur.execute(statement)
    result=cur.fetchall()
    articles=[list(i) for i in result]
    #print(articles)
    conn.commit()
    conn.close()
    counter=1
    for items in articles:
        articleLib.update({items[1]:[items[2],items[3],counter]})
        counter+=1
    #print(articleLib)

def pick_news():
    check=0
    selection=input('Please enter an article index number\n')
    try:
        selection=int(selection)
        for items in articleLib:
            if articleLib[items][2]==selection:
                print(articleLib[items][0])
                check+=1
        if check==0:
            print('invalid article index, please try again')
            articles()
    except:
        print('invalid article index, please try again')
        articles()
    news()

def articles():
    counter=1
    for items in articleLib:
        print(articleLib[items][2], items)
    pick_news()

#function to handle the shopping site
def shop():
    command_list=['home']
    print('minigame not yet implemented, please return to home')
    comIn(command_list)

#function to handle the Nintendo network Oz
def Nintendo():
    command_list=['home']
    print('minigame not yet implemented, please return to home')
    comIn(command_list)

#function to handle the Nestle-Yutani network
def NYnet():
    command_list=['home']
    print('minigame not yet implemented, please return to home')
    comIn(command_list)

#function to handle the Dragon Palace network
def dragonPalace():
    browse_history.append('dragonPalace')
    command_list=['home','request']
    print('''$$$$$Dragon Palace Casino$$$$$\n\nWelcome to the most exclusive gambling establishment in New Seattle. We offer baccarat, poker, and roullette in the most distinguished setting in all of the Sick City.  Our staff provides the most premium experience for the most discerning gamblers.\n|||||Booking\nrequest\n\n|||||employees\nlogin''')
    comIn(command_list)

#function to handle the Youtube links
def vibe():
    global browse_history
    browse_history.append('vibe')
    command_list=['home','outrun','vaporwave','greenhouse','hack']
    print('''New Seattle NSNQ93.9 - Sick City Radio\n\n*player warning, these commands will open Youtube*\n\n|||||The Three Kinds of Music|||||\noutrun\nvaporwave\ngreenhouse\n\n|||||Support Local Events|||||\nShots Night at Curtain\nKinetic Karaoke at Crisis\nMen Under 25 Drink Free at the Crystal Box\nCybernight at DISCORD\n\n|||||Return to Home\nhome''')
    comIn(command_list)

#the hacking function
def hack():
    global browse_history
    browse_history.append('hack')
    hack_target=browse_history[-2]
    print('|||HACKING|||')
    if hack_target=='vibe':
        command_list=['sanic','home','vibe']
    else:
        command_list=['home']
    comIn(command_list)
    

#music functions from Vibe, they all open youtube in your browser.
def outrun():
    print('|||||Odysseus with the kinetic beats for your big score|||||')
    webbrowser.open('https://www.youtube.com/watch?v=DGkzmd66oaY&t=49s')
    vibe()

def vaporwave():
    print('|||||Reve Lucide here to help you drift into cyberspace|||||')
    webbrowser.open('https://www.youtube.com/watch?v=ODFY81dDpjQ')
    vibe()

def greenhouse():
    print('||||All you hypersonics better get your sun and water to keep up with these beats|||||')
    webbrowser.open('https://www.youtube.com/watch?v=xbAtMG9f6t4')
    vibe()

def sanic(): #the hidden track, this is a vanity hack
    print('GOTTA GO FAST')
    webbrowser.open('https://www.youtube.com/watch?v=tCRJjcTfwQk')
    vibe()

def request():
    print('''Please allow between 6 and 8 months for new member booking.  Your request is recorded.''')
    command_list=['home','dragonPalace']
    comIn(command_list)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||Functions Dictionary

#the command library lets us use straight words to invoke functions, it is global so that hidden functions can be accepted.  This will be done through the hack keyword, which will open the hacking function to do tasks.


#||||||||||||||||||||||||||||||||||||||||||||||||||||||Mainline Functions

get_news()
home()
