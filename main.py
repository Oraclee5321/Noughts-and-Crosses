import tkinter as tk
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
    def changeState(self, button):
        button['state'] = 'disabled'

    def buttonClick(self, button):
        if self.player1.getTurn():
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
        if b1['text'] == b2['text'] == b3['text'] == player.getIcon():
            return(True)
        elif b4['text'] == b5['text'] == b6['text'] == player.getIcon():
            return(True)
        elif b7['text'] == b8['text'] == b9['text'] == player.getIcon():
            return(True)
        elif b1['text'] == b4['text'] == b7['text'] == player.getIcon():
            return(True)
        elif b2['text'] == b5['text'] == b8['text'] == player.getIcon():
            return(True)
        elif b3['text'] == b6['text'] == b9['text'] == player.getIcon():
            return(True)
        elif b1['text'] == b5['text'] == b9['text'] == player.getIcon():
            return(True)
        elif b3['text'] == b5['text'] == b7['text'] == player.getIcon():
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

Game = Game(player, computer)
        
#create a window
win = tk.Tk()
win.title("Python GUI")
#open window

b1 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b1))
b2 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b2))
b3 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b3))

b4 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b4))
b5 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b5))
b6 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b6))
b7 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b7))
b8 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b8))
b9 = ttk.Button(win, text="", command=lambda: Game.buttonClick(b9))



b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

win.mainloop()



