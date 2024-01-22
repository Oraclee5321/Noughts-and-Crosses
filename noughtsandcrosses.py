import tkinter as tk
from tkinter import ttk
import random
import time

class Player():  # Class for players in the game
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.ties = 0
        self.losses = 0
        self.turn = False
        self.icon = ""
        self.iscomputer = False

    def getName(self):
        return self.name

    def setComputer(self, value):
        self.iscomputer = value

    def getTurn(self):
        return self.turn

    def getIcon(self):
        return self.icon

    def setIcon(self, icon):
        self.icon = icon

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def setTie(self, value):
        self.ties = value

    def getTie(self):
        return self.ties

    def setLoss(self, value):
        self.losses = value

    def getLoss(self):
        return self.losses


class Game():  # Class for the game itself
    def __init__(self,root):
        self.root = root
        self.player1 = None
        self.player2 = None
        self.turn_count = 0
        self.enabled_buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = ""
        self.players = []
        self.mainMenu()

    def __del__(self):  # Main menu reappears on destruction of object
        self.root.deiconify()

    def mainMenu(self):  # Main menu of the Game
        self.menu_window = tk.Toplevel()  # Creates new window
        self.iscomputer = tk.IntVar(None, 2)
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
        self.root.withdraw()  # Hides initial menu

    def editPlayerTwo(self, edit_type):  # Hides player 2 entry fields if computer is selected
        if edit_type == 1:
            self.player2_name.grid_remove()
            self.player2_name_label.grid_remove()
        elif edit_type == 2:
            self.player2_name.grid()
            self.player2_name_label.grid()
        pass

    def checkEntries(self):  # Makes sure that all players are given a name
        p1_name = self.player1_name.get()
        if len(p1_name) == 0:
            self.player1_name_label.configure(text=(self.player1_name_label.cget("text") + "Required**"))
        if self.iscomputer.get() == 2:
            p2_name = self.player2_name.get()
            computer = False  # Makes sure they are not set to computer
            if len(p2_name) == 0:
                self.player2_name_label.configure(text=(self.player2_name_label.cget("text") + "Required**"))
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
        for player in self.players:  # Assign icons to players
            icon = random.choice(icons)
            player.setIcon(icon)
            icons.remove(icon)
        self.menu_window.destroy()  # Removes menu and all children
        self.setupBoard()

    def gameRestart(self):  # Resets board for another game
        self.game_window.destroy()
        self.enabled_buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.setupBoard()

    def gameClose(self):  # Opens up original menu and destroys the game
        self.root.deiconify()
        self.game_window.destroy()
        return

    def setupBoard(self):
        self.current_player = random.randint(0, 1)  # Selects first player to start
        self.players[self.current_player].turn = True
        self.game_window = tk.Toplevel()
        self.game_window.geometry("300x300")
        self.game_window.resizable(False, False)
        self.game_window.title(("Turn Number: " + str(self.turn_count)))
        self.b1 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b1))
        self.b2 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b2))
        self.b3 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b3))
        self.b4 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b4))
        self.b5 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b5))
        self.b6 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b6))
        self.b7 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b7))
        self.b8 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b8))
        self.b9 = ttk.Button(self.game_window, text="", command=lambda: self.buttonClick(self.b9))
        self.userturn = tk.Label(self.game_window,
                                 text=("It is: " + self.players[self.current_player].getName() + "'s Turn"))
        self.userturn.grid(row=3, column=0, columnspan=3, sticky="news")
        self.b1.grid(row=0, column=0, sticky="news")
        self.b2.grid(row=0, column=1, sticky="news")
        self.b3.grid(row=0, column=2, sticky="news")
        self.b4.grid(row=1, column=0, sticky="news")
        self.b5.grid(row=1, column=1, sticky="news")
        self.b6.grid(row=1, column=2, sticky="news")
        self.b7.grid(row=2, column=0, sticky="news")
        self.b8.grid(row=2, column=1, sticky="news")
        self.b9.grid(row=2, column=2, sticky="news")
        for row in range(4):  # Makes it so buttons fill up screen
            self.game_window.rowconfigure(row, weight=1)
        for column in range(3):
            self.game_window.columnconfigure(column, weight=1)
        self.root.withdraw()  # Makes sure the initial menu is hidden still
        if self.player2.getTurn() and self.player2.iscomputer:  # If computer starts first
            self.userturn.configure(text=("It is: " + self.player2.getName() + "'s Turn"))
            self.game_window.update()  # UI updates while before sleep
            time.sleep(1)
            self.computerTurn()

    def computerTurn(self):
        computer_choice = random.choice(self.enabled_buttons)
        self.b = getattr(self, "b" + str(computer_choice))  # Retrieves a random button from the class
        self.b.invoke()  # Button is clicked digitally so the command happens

    def changeState(self, button):  # Disables a button once it is clicked
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
            self.userturn.configure(text=("It is: " + self.player2.getName() + "'s Turn"))
        else:
            button.config(text=self.player2.getIcon())
            self.changeState(button)
            self.player1.turn = True
            self.player2.turn = False
            self.userturn.configure(text=("It is: " + self.player1.getName() + "'s Turn"))
        self.turn_count += 1
        self.game_window.title(("Turn Number: " + str(self.turn_count)))
        if self.turn_count > 10:
            self.tie()
            return
        elif self.turn_count >= 5:
            if not self.player1.getTurn():
                if self.checkWin(self.player1):
                    self.player2.setLoss(self.player2.getLoss() + 1)
                    self.endGame(self.player1)
            elif not self.player2.getTurn():
                if self.checkWin(self.player2):
                    self.player1.setLoss(self.player1.getLoss() + 1)
                    self.endGame(self.player2)
        if self.player2.getName() == "Computer" and self.player2.turn:  # Only way I could think of having the computer take its turn
            self.game_window.update()
            time.sleep(1)
            self.computerTurn()

    def checkWin(self, player):  # Hardcoded win conditions
        if self.b1['text'] == self.b2['text'] == self.b3['text'] == player.getIcon():
            return True
        elif self.b4['text'] == self.b5['text'] == self.b6['text'] == player.getIcon():
            return True
        elif self.b7['text'] == self.b8['text'] == self.b9['text'] == player.getIcon():
            return True
        elif self.b1['text'] == self.b4['text'] == self.b7['text'] == player.getIcon():
            return True
        elif self.b2['text'] == self.b5['text'] == self.b8['text'] == player.getIcon():
            return True
        elif self.b3['text'] == self.b6['text'] == self.b9['text'] == player.getIcon():
            return True
        elif self.b1['text'] == self.b5['text'] == self.b9['text'] == player.getIcon():
            return True
        elif self.b3['text'] == self.b5['text'] == self.b7['text'] == player.getIcon():
            return True
        else:
            return

    def createEndButtons(self):  # Just creates buttons at the end of a game
        self.player1.turn = False
        self.player2.turn = False
        new_game_button = ttk.Button(self.game_window, text="Play Another?", command=lambda: self.gameRestart())
        end_game_button = ttk.Button(self.game_window, text="Quit", command=lambda: self.gameClose())
        new_game_button.grid(row=5, column=0, sticky="news")
        end_game_button.grid(row=5, column=1, sticky="news")
        return

    def displayStats(self):  # Displays the players stats at the end of a game
        player1_stats = tk.Label(self.game_window, text=self.player1.getName() + "'s Stats:\n Wins:" + str(
            self.player1.getScore()) + "\n Losses: " + str(self.player1.getLoss()))
        player2_stats = tk.Label(self.game_window, text=self.player2.getName() + "'s Stats:\n Wins:" + str(
            self.player2.getScore()) + "\n Losses: " + str(self.player2.getLoss()))
        total_ties = tk.Label(self.game_window, text="Total Ties: " + str(self.player1.getTie()))
        player1_stats.grid(row=4, column=0, sticky="news")
        player2_stats.grid(row=4, column=1, sticky="news")
        total_ties.grid(row=4, column=2, sticky="news")

    def tie(self):
        self.turn_count = 0
        self.userturn.configure(text="Game Tied")
        self.player1.setTie(self.player1.getTie() + 1)
        self.player2.setTie(self.player2.getTie() + 1)
        self.displayStats()
        self.createEndButtons()
        return

    def endGame(self, player):
        self.turn_count = 0
        self.player1.turn = False
        self.player2.turn = False
        player.setScore(player.getScore() + 1)
        for item in self.enabled_buttons:  # Disables all remaining buttons in the game
            button = self.b = getattr(self, "b" + str(item))
            button['state'] = "disabled"
        self.userturn.configure(text=("Winner is : " + player.getName()))
        self.displayStats()
        self.createEndButtons()
        return
