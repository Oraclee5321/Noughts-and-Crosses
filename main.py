import tkinter as tk
import random
import sys
from tkinter import ttk

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn = False
        self.icon = ""
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def getTurn(self):
        return self.turn
    def getIcon(self):
        return self.icon
    def setIcon(self, icon):
        self.icon = icon
    def setScore(self, score):
        self.score = score

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player1.turn = True
        self.player1.setIcon("X")
        self.player2 = player2
        self.player2.setIcon("O")
        self.turn_count = 0
        self.enabled_buttons = [1,2,3,4,5,6,7,8,9]
        self.setupBoard()

    def setupBoard(self):
        self.b1 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b1))
        self.b2 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b2))
        self.b3 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b3))
        self.b4 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b4))
        self.b5 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b5))
        self.b6 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b6))
        self.b7 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b7))
        self.b8 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b8))
        self.b9 = ttk.Button(win, text="", command=lambda: self.buttonClick(self.b9))
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)


    def computerTurn(self):
        computer_choice = random.choice(self.enabled_buttons)
        self.b = getattr(self, "b" + str(computer_choice))
        self.b.invoke()


    def changeState(self, button):
        button['state'] = 'disabled'
        #self.enabled_buttons.remove(int(button._name[-1]))
        print(self.enabled_buttons)



    def buttonClick(self, button):
        if self.player1.getTurn():
            self.turn_count += 1
            button.config(text=self.player1.getIcon())
            self.changeState(button)
            self.player1.turn = False
            self.player2.turn = True
        else:
            button.config(text=self.player2.getIcon())
            self.changeState(button)
            self.player1.turn = True
            self.player2.turn = False

        self.turn_count += 1
        if self.turn_count == 9:
            print("Tie")
            return
        elif self.turn_count >= 5:
            if not self.player1.getTurn():
                if self.checkWin(self.player1):
                    self.endGame(self.player1)                
            elif not self.player2.getTurn():
                if self.checkWin(self.player2):
                    self.endGame(self.player2)

    def checkWin(self,player):
        if self.b1['text'] == self.b2['text'] == self.b3['text'] == player.getIcon():
            return(True)
        elif self.b4['text'] == self.b5['text'] == self.b6['text'] == player.getIcon():
            return(True)
        elif self.b7['text'] == self.b8['text'] == self.b9['text'] == player.getIcon():
            return(True)
        elif self.b1['text'] == self.b4['text'] == self.b7['text'] == player.getIcon():
            return(True)
        elif self.b2['text'] == self.b5['text'] == self.b8['text'] == player.getIcon():
            return(True)
        elif self.b3['text'] == self.b6['text'] == self.b9['text'] == player.getIcon():
            return(True)
        elif self.b1['text'] == self.b5['text'] == self.b9['text'] == player.getIcon():
            return(True)
        elif self.b3['text'] == self.b5['text'] == self.b7['text'] == player.getIcon():
            return(True)
        else:
            return
        
    def endGame(self,player):
        print("Winner is: ", player.getName())
        self.turn_count = 0
        self.player1.turn = False
        self.player2.turn = False
        player.setScore(player.getScore() + 1)
        pass
        

        


computer = Player("Computer")
player = Player("Player")

        
#create a window
win = tk.Tk()
win.title("Noughts and Crosses")
#open window

Game = Game(player, computer)

win.mainloop()



