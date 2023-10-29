import tkinter as t # ini apa????
from time import sleep
import random
#
userInput = ""
computerInput = ""
def fileOp(fileName, operation='r', content=''):
    # nama file
    # content
    
    # add/create : buat file baru (w)
    # edit/update(append) : edit existing file (a)
    # view/read : hanya baca - default (r)
    file = open(fileName,operation)
    if operation!='r':
        file.write(content)
    else:
        content = file.readlines()
    file.close()
    return content

highScore = int(fileOp("score")[0])
userScore = 0
pcScore = 0

def cek_winner():
    global userScore, pcScore, highScore
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
    if userScore>highScore:
        fileOp("score","w",str(userScore))
        highScore = int(fileOp("score")[0])
    labelUserScore.config(text=userScore)
    labelPcScore.config(text=pcScore)
    labelHighScore.config(text=highScore)
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



labelHighScore = t.Label(window, text=highScore,width=15, font=("Arial",20))
labelHighScore.grid(column=2,row=5)

window.mainloop()
