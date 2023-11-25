import tkinter as t #lakukan import tkiner
from time import sleep
import random
import socket, json
userInput = ""
computerInput = ""
#socketed
currData = {}
serverIp = "127.0.0.1"
def send_choice(choice):
    global currData
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((serverIp, 5555))
        client_socket.send(choice.encode())
        result_msg = client_socket.recv(1024).decode()
        print(result_msg)
        currData = json.loads(result_msg)


userScore = 0
pcScore = 0

def cek_winner():
    global userScore, pcScore
    msg = ""
    if userInput == computerInput:
        labelPcInput.config(bg="orange")
        labelUserInput.config(bg="orange")
        msg = "It's a tie!"
    elif userInput == 'gun':
        labelPcInput.config(bg="red")
        labelUserInput.config(bg="green")
        userScore=userScore+1 # userScore+=1
        msg = "You win! cmon man its unfair!!!."
    elif userInput == 'shield' or computerInput=='shield':
        labelPcInput.config(bg="orange")
        labelUserInput.config(bg="orange")
        msg = "It's a tie! Shield blocks everything."
    elif (
        (userInput == 'rock' and computerInput == 'scissors') or
        (userInput == 'paper' and computerInput == 'rock') or
        (userInput == 'scissors' and computerInput == 'paper')
    ):
        labelPcInput.config(bg="red")
        labelUserInput.config(bg="green")
        userScore=userScore+1 # userScore+=1
        msg = "You win!"
    else:
        labelPcInput.config(bg="green")
        labelUserInput.config(bg="red")
        pcScore=pcScore+1 # userScore+=1
        msg = "Computer wins!"
    labelUserScore.config(text=userScore)
    labelPcScore.config(text=pcScore) 
    return msg

def computer():
    global computerInput
    choices = ['rock', 'paper', 'scissors','shield','gun']
    computerInput =  random.choice(choices)
    labelPcInput.config(text=computerInput)
    labelUserInput.config(text=userInput)
    print(cek_winner())
def rock():
    global userInput
    userInput = "rock"
    computer()
def paper():
    global userInput
    userInput = "paper"
    computer()
def scissor():
    global userInput
    userInput = "scissor"
    computer()
def gun():
    global userInput
    userInput = "gun"
    computer()
def shield():
    global userInput
    userInput = "shield"
    computer()
window = t.Tk()
#window.geometry("300x300")
labelPcInput = t.Label(window, text="😲",width=15, font=("Arial",20))
labelPcInput.grid(column=0,row=0,rowspan=5)

labelUserInput = t.Label(window, text="🎮",width=15, font=("Arial",20))
labelUserInput.grid(column=1,row=0,rowspan=5)

btnRock = t.Button(window, text="Rock",width=15,command=rock)
btnRock.grid(column=2,row=0)
btnPaper = t.Button(window, text="Paper",width=15,command=paper)
btnPaper.grid(column=2,row=1)
btnScissor = t.Button(window, text="Scissor",width=15,command=scissor)
btnScissor.grid(column=2,row=2)
btnGun = t.Button(window, text="Gun",width=15,command=gun)
btnGun.grid(column=2,row=3)
btnShield = t.Button(window, text="Shield",width=15,command=shield)
btnShield.grid(column=2,row=4)

labelPcScore = t.Label(window, text="0",width=15, font=("Arial",20))
labelPcScore.grid(column=0,row=5)

labelUserScore = t.Label(window, text="0",width=15, font=("Arial",20))
labelUserScore.grid(column=1,row=5)

window.mainloop()
