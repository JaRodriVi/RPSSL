# RPSSL

import simplegui
import random
import math


# Rock-paper-scissors-lizard-Spock template
#
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# start message:

message= " Time to play "
message2= " Have fun!! "

# helper functions

def name_to_number(name):
    # this convert the name to a number.
    if name=="rock":
        return 0
    elif name== "paper":
        return 2
    elif name=="scissors":
        return 4
    elif name=="lizard":
        return 3
    elif name=="Spock":
        return 1
        
        
def number_to_name(number):
    # this convert the number to one of the options in the game.
    if number==0:
        return "rock"
    elif number==2 :
        return "paper"
    elif number==4:
        return "scissors"
    elif number==3:
        return "lizard"
    elif number==1:
        return "Spock"
    

def rpsls(choice): 
    # this is the game
    global cpu_name
    global winner_message
    
    player = name_to_number(choice)
    cpu = random.randrange(0,4)
    cpu_name = number_to_name(cpu)
    
    # compute difference of comp_number and player_number modulo five
    winner = (player - cpu)%5
    # use if/elif/else to determine winner, print winner message
    
    if (winner == 3 or winner== 4):
        winner_message = "CPU wins :("
        
    elif (winner == 1 or winner== 2):
        winner_message = "You win!!!" 

    else:
        winner_message = "  TIE  "

    
    
# Handler for input field
def get_guess(guess):
    if not( guess=="rock" or guess=="Spock" or guess=="paper"
            or guess=="scissors" or guess=="lizard"):
        print "Error: Bad input" + guess + "to rpsls"
        return
    else:
        rpsls(guess)

def rock():
    get_guess("rock")
    global message
    global message2
    message = "Rock vs " + cpu_name
    message2 = winner_message
    
def spock():
    get_guess("Spock")
    global message
    global message2
    message = "Spock vs " + cpu_name
    message2 = winner_message
    
def paper():
    get_guess("paper")
    global message
    global message2
    message = "Paper vs " + cpu_name
    message2 = winner_message

def lizard():
    get_guess("lizard")
    global message
    global message2
    message = "Lizard vs " + cpu_name
    message2 = winner_message
    
def scissors():
    get_guess("scissors")
    global message
    global message2
    message = "Scissors vs " + cpu_name
    message2 = winner_message
    

def draw(canvas):
    canvas.draw_text(message, [60,75], 30, "Red")
    canvas.draw_text(message2,[80,125], 30, "Red")


# Create frame and assign callbacks to event handlers

f = simplegui.create_frame("RPSLS", 300, 200)
f.add_button("Rock",rock,100)
f.add_button("Spock",spock,100)
f.add_button("Paper",paper,100)
f.add_button("Lizard",lizard,100)
f.add_button("Scissors",scissors,100)
f.set_draw_handler(draw)


# Start the frame animation
f.start()
