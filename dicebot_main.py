import socket
import random


ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket-variable for connection
server = "chat.freenode.net" # Server name which to connect, may be changed at will
channel = "##bot-testing" # Channel under the server which you want to use. May be changed at will
botnick = "dicebot" # Bot's name
adminname = "SugarD" # User's nickname on IRC.
exitcode = "Kiitos pelaamisesta " + botnick + "!"
port = "6667"  # Variable for IRC port
players = []  # List for players. Default = empty
hand1 = [1, 1]  # Hand for player 1. Default set = 1,1
hand2 = [1, 1]  # Hand for player 2. Default set = 1,1


'''Function for establishing a connection to IRC'''
def connect_to_irc(sname, pnum, bnick):
    ircsocket.connect((sname,pnum)) # Establish connection to a server
    ircsocket.send(bytes('USER ' + bnick + " " + bnick + " " + bnick + " " + bnick + "\n", "UTF-8")) # Filling a form to set all settings to our botnick
    ircsocket.send(bytes("NICK "+bnick+"\n","UTF-8")) # Assigning nick to the bot


'''Function for connecting to a channel'''
def join_channel(chn):
    ircsocket.send(bytes("JOIN "+chn+"\n","UTF-8"))
    ircmsg = ""

    while ircmsg.find("End of /NAMES list.")==1:
        ircmsg=ircsocket.recv(2048).decode("UTF-8")
        ircmsg=ircmsg.strip('\n\r')
        print(ircmsg)


'''Function to respond to server pings'''
def ping():
    ircsocket.send(bytes("PONG :pingis\n","UTF-8"))


'''Sends a message to the target'''
def send_message(msg, target=channel):
    ircsocket.send(bytes("PRIVMSG " + target + " :" + msg + "\n", "UTF-8"))

'''Sets two dice numbers to hand1 and hand2'''
def set_hands():
    hand1[0] = random.randint(1,6)
    hand1[1] = random.randint(1,6)
    hand2[0] = random.randint(1,6)
    hand2[1] = random.randint(1,6)


'''Resets hands to default'''
def reset_hands():
    hand1[0] = 1
    hand1[1] = 1
    hand2[0] = 1
    hand2[1] = 1


'''Sets players for the game'''
def set_players(name1, name2):
    players.append(name1 + name2)



'''Main function. In infinite loop'''
def main():
    join_channel(channel)
    while 1:
        ircmsg = ircsocket.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!', 1)[0][1]

            message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]

            '''if len(name) < 17:
                if message.find(botnick +".challenge") != -1:
                    
                    Enter function to challenge a nickname here
                    '''






