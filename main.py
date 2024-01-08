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
        self.iscomputer = False

    def getName(self):
        return self.name
    def setComputer(self, value):
        self.iscomputer = value
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
    def __init__(self):
        self.turn_count = 0
        self.enabled_buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = ""
        self.players = []
        self.mainMenu()
    def __del__(self): # Used for debug
        print("Deleted")
    def mainMenu(self):
        self.menu_window = tk.Toplevel()
        self.iscomputer = tk.IntVar(None,2)
        self.playing_computer_label = tk.Label(self.menu_window, text="Playing the Computer?")
        self.playing_computer_label.grid(row=0, column=0)
        self.playing_computer_yes = ttk.Radiobutton(self.menu_window, text="Yes", variable=self.iscomputer, value=1,
                                                    command=lambda: self.editPlayerTwo(self.iscomputer.get()))
        self.playing_computer_yes.grid(row=0, column=1)
        self.playing_computer_no = ttk.Radiobutton(self.menu_window, text="No", variable=self.iscomputer, value=2,
                                                   command=lambda: self.editPlayerTwo(self.iscomputer.get()))
        self.playing_computer_no.grid(row=0, column=2)
        self.player1_name = tk.Entry(self.menu_window, width=20)
        self.player1_name_label = tk.Label(self.menu_window, text="Player 1 Name:")
        self.player1_name.grid(row=1, column=1)
        self.player1_name_label.grid(row=1, column=0)
        self.player2_name = tk.Entry(self.menu_window, width=20)
        self.player2_name_label = tk.Label(self.menu_window, text="Player 2 Name:")
        self.player2_name.grid(row=2, column=1)
        self.player2_name_label.grid(row=2, column=0)
        self.continue_button = ttk.Button(self.menu_window, text="Play", command=lambda: self.checkEntries())
        self.continue_button.grid(row=3, column=1)
        root.withdraw()

    def editPlayerTwo(self, edit_type):
        if edit_type == 1:
            self.player2_name.grid_remove()
            self.player2_name_label.grid_remove()
        elif edit_type == 2:
            self.player2_name.grid()
            self.player2_name_label.grid()
        pass

    def checkEntries(self):
        p1_name = self.player1_name.get()
        if len(p1_name) == 0:
            self.player1_name_label.configure(text=(self.player1_name_label.cget("text")+"Required**"))
            return
        if self.iscomputer.get() == 2:
            p2_name = self.player2_name.get()
            computer = False
            if len(p2_name) == 0:
                self.player2_name_label.configure(text=(self.player2_name_label.cget("text") + "Required**"))
                return
            pass
        elif self.iscomputer.get() == 1:
            p2_name = "Computer"
            computer = True
        self.player1 = Player(p1_name)
        self.player2 = Player(p2_name)
        self.player2.setComputer(computer)
        self.players.append(self.player1)
        self.players.append(self.player2)
        icons = ["X", "O"]
        for player in self.players:
            icon = random.choice(icons)
            player.setIcon(icon)
            icons.remove(icon)
        self.menu_window.destroy()
        self.setupBoard()
    def gameRestart(self):
        self.game_window.destroy()
        self.enabled_buttons = [1,2,3,4,5,6,7,8,9]
        self.setupBoard()

    def gameClose(self):
        root.deiconify()
        self.game_window.destroy()
        return
    def setupBoard(self):
        self.current_player = random.randint(0,1)
        self.players[self.current_player].turn = True
        self.game_window = tk.Toplevel()
        self.game_window.geometry("300x300")
        self.game_window.resizable(False,False)
        self.game_window.title(("Turn Number: "+str(self.turn_count)))
        self.b1 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b1))
        self.b2 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b2))
        self.b3 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b3))
        self.b4 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b4))
        self.b5 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b5))
        self.b6 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b6))
        self.b7 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b7))
        self.b8 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b8))
        self.b9 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b9))
        self.userturn = tk.Label(self.game_window, text=("It is: "+ self.players[self.current_player].getName()+ "'s Turn"))
        self.userturn.grid(row=3,column=0, columnspan=3, sticky="news")
        self.b1.grid(row=0, column=0, sticky="news")
        self.b2.grid(row=0, column=1, sticky="news")
        self.b3.grid(row=0, column=2, sticky="news")
        self.b4.grid(row=1, column=0, sticky="news")
        self.b5.grid(row=1, column=1, sticky="news")
        self.b6.grid(row=1, column=2, sticky="news")
        self.b7.grid(row=2, column=0, sticky="news")
        self.b8.grid(row=2, column=1, sticky="news")
        self.b9.grid(row=2, column=2, sticky="news")
        for row in range(4):
            self.game_window.rowconfigure(row,weight=1)
        for column in range(3):
            self.game_window.columnconfigure(column, weight=1)
        root.withdraw()

    def computerTurn(self):
        computer_choice = random.choice(self.enabled_buttons)
        self.b = getattr(self, "b" + str(computer_choice))
        self.b.invoke()

    def changeState(self, button):
        try:
            button['state'] = 'disabled'
            self.enabled_buttons.remove(int(button._name[-1]))
        except ValueError:
            self.enabled_buttons.remove(1)

    def buttonClick(self, button):
        if self.player1.getTurn():
            button.config(text=self.player1.getIcon())
            self.changeState(button)
            self.player1.turn = False
            self.player2.turn = True
            self.userturn.configure(text=("It is: "+ self.player2.getName()+"'s Turn"))
        else:
            button.config(text=self.player2.getIcon())
            self.changeState(button)
            self.player1.turn = True
            self.player2.turn = False
            self.userturn.configure(text=("It is: " + self.player1.getName() + "'s Turn"))
        self.turn_count += 1
        self.game_window.title(("Turn Number: " + str(self.turn_count)))
        if self.turn_count == 9:
            self.tie()
            return
        elif self.turn_count >= 5:
            if not self.player1.getTurn():
                if self.checkWin(self.player1):
                    self.endGame(self.player1)
            elif not self.player2.getTurn():
                if self.checkWin(self.player2):
                    self.endGame(self.player2)

    def checkWin(self, player):
        if self.b1['text'] == self.b2['text'] == self.b3['text'] == player.getIcon():
            return (True)
        elif self.b4['text'] == self.b5['text'] == self.b6['text'] == player.getIcon():
            return (True)
        elif self.b7['text'] == self.b8['text'] == self.b9['text'] == player.getIcon():
            return (True)
        elif self.b1['text'] == self.b4['text'] == self.b7['text'] == player.getIcon():
            return (True)
        elif self.b2['text'] == self.b5['text'] == self.b8['text'] == player.getIcon():
            return (True)
        elif self.b3['text'] == self.b6['text'] == self.b9['text'] == player.getIcon():
            return (True)
        elif self.b1['text'] == self.b5['text'] == self.b9['text'] == player.getIcon():
            return (True)
        elif self.b3['text'] == self.b5['text'] == self.b7['text'] == player.getIcon():
            return (True)
        else:
            return

    def createEndButtons(self):
        self.player1.turn = False
        self.player2.turn = False
        new_game_button = ttk.Button(self.game_window, text="Play Another?", command=lambda: self.gameRestart())
        end_game_button = ttk.Button(self.game_window, text="Quit", command=lambda: self.gameClose())
        new_game_button.grid(row=4, column=0, sticky="news")
        end_game_button.grid(row=4, column=1, sticky="news")
        return
    def tie(self):
        self.userturn.configure(text=("Game Tied"))
        self.createEndButtons()
        return
    def endGame(self, player):
        self.turn_count = 0
        self.player1.turn = False
        self.player2.turn = False
        player.setScore(player.getScore() + 1)
        for item in self.enabled_buttons:
            button = self.b = getattr(self, "b" + str(item))
            button['state'] = "disabled"
        self.userturn.configure(text=("Winner is : "+player.getName()+"\n"+player.getName()+" Has "+ str(player.getScore())+ " Wins!"))
        self.createEndButtons()
        return


def createGame():
    noughts_crosses = Game()


def nameChange():
    pass


def createMainMenu():
    root = tk.Tk()
    root.title("Python Application")
    noughts_crosses_button = ttk.Button(root, text="Noughts and Crosses", command=lambda: createGame())
    name_change_button = ttk.Button(root, text="Company Name Change", command=lambda: nameChange())
    noughts_crosses_button.grid(row=0, column=0)
    name_change_button.grid(row=1, column=0)
    return root


root = createMainMenu()

root.mainloop()
