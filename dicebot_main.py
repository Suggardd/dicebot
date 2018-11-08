import socket

ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket-variable for connection
server = "chat.freenode.net" # Server name which to connect, may be changed at will
channel = "##bot-testing" # Channel under the server which you want to use. May be changed at will
botnick = "dicebot" # Bot's name
adminname = "SugarD" # User's nickname on IRC.
exitcode = "Kiitos pelaamisesta " + botnick + "!"
port = "6667" # Variable for IRC port


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
    ircsocket.send(bytes("PRIVMSG "+target +" :"+msg+"\n","UTF-8"))


'''Main function'''
def main():
    join_channel(channel)
    while 1:
        



