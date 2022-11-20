"""
Title: tic-tac-toe.py
Author: Joseph Scott
Build Date: December 2019
Description: Local GUI 2 player game of tic tac toe.
"""

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        #Set window size and title
        self.main_window.minsize(500,250)
        self.main_window.title("Tic-Tac-Toe")
        self.main_window.configure(background='black')

        #Create frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.info_frame.config(bg="black")
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.config(bg="black")
        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle_frame.config(bg="black")
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.config(bg="black")
        self.option_frame = tkinter.Frame(self.main_window)
        self.option_frame.config(bg="black")

        #init player text and player number
        self.playerText = tkinter.StringVar()
        self.playerText.set("Player 1")
        self.playerNum = tkinter.IntVar()
        self.playerNum.set(1)

        #init string vars for each button
        self.btn_text00 = tkinter.StringVar()
        self.btn_text00.set("")
        self.btn_text10 = tkinter.StringVar()
        self.btn_text10.set("")
        self.btn_text20 = tkinter.StringVar()
        self.btn_text20.set("")
        self.btn_text01 = tkinter.StringVar()
        self.btn_text01.set("")
        self.btn_text11 = tkinter.StringVar()
        self.btn_text11.set("")
        self.btn_text21 = tkinter.StringVar()
        self.btn_text21.set("")
        self.btn_text02 = tkinter.StringVar()
        self.btn_text02.set("")
        self.btn_text12 = tkinter.StringVar()
        self.btn_text12.set("")
        self.btn_text22 = tkinter.StringVar()
        self.btn_text22.set("")

        #top info, current player turn
        self.topLabel = tkinter.Label(self.info_frame, textvariable=self.playerText, font=("Consolas 30 bold"), fg="White", bg="black")
        self.topLabel.pack(padx=5, pady=20)

        #first row of tiles
        self.pos00Btn = tkinter.Button(self.top_frame, textvariable=self.btn_text00, command=lambda : self.clicked(self.pos00Btn, self.btn_text00, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos10Btn = tkinter.Button(self.top_frame, textvariable=self.btn_text10, command=lambda : self.clicked(self.pos10Btn, self.btn_text10, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos20Btn = tkinter.Button(self.top_frame, textvariable=self.btn_text20, command=lambda : self.clicked(self.pos20Btn, self.btn_text20, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos00Btn.pack(side='left', padx=5, pady=5)
        self.pos10Btn.pack(side='left', padx=5, pady=5)
        self.pos20Btn.pack(side='left', padx=5, pady=5)

        #second row of tiles
        self.pos01Btn = tkinter.Button(self.middle_frame, textvariable=self.btn_text01, command=lambda : self.clicked(self.pos01Btn, self.btn_text01, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos11Btn = tkinter.Button(self.middle_frame, textvariable=self.btn_text11, command=lambda : self.clicked(self.pos11Btn, self.btn_text11, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos21Btn = tkinter.Button(self.middle_frame, textvariable=self.btn_text21, command=lambda : self.clicked(self.pos21Btn, self.btn_text21, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos01Btn.pack(side='left', padx=5, pady=5)
        self.pos11Btn.pack(side='left', padx=5, pady=5)
        self.pos21Btn.pack(side='left', padx=5, pady=5)

        #third row of tiles
        self.pos02Btn = tkinter.Button(self.bottom_frame, textvariable=self.btn_text02, command=lambda : self.clicked(self.pos02Btn, self.btn_text02, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos12Btn = tkinter.Button(self.bottom_frame, textvariable=self.btn_text12, command=lambda : self.clicked(self.pos12Btn, self.btn_text12, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos22Btn = tkinter.Button(self.bottom_frame, textvariable=self.btn_text22, command=lambda : self.clicked(self.pos22Btn, self.btn_text22, self.playerNum, self.playerText), width = 5, bg = "white", font=("Consolas 30 bold"))
        self.pos02Btn.pack(side='left', padx=5, pady=5)
        self.pos12Btn.pack(side='left', padx=5, pady=5)
        self.pos22Btn.pack(side='left', padx=5, pady=5)


        #setup quit and reset
        self.quit = tkinter.Button(self.option_frame, text='Quit', command=self.main_window.destroy, width = 10)
        self.reset = tkinter.Button(self.option_frame, text='Reset', command=self.resertAll, width = 10)
        self.quit.pack(side='left', padx=5, pady=25)
        self.reset.pack(side='left', padx=5, pady=25)

        #pack frames
        self.info_frame.pack()
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.option_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    #function called when position button is clicked
    def clicked(self, button, buttonsText, playerNum, playerText):

        #disable button, its cant be clicked again
        button['state'] = 'disabled'
        #init winner state
        winner = -1

        #if button clicked on player 1s turn
        #set button text to X
        #set player turn text to 2 for next turn
        #call check win function, returns the winner, -1 if no winner detected
        #sets player num to 2 for their turn
        if playerNum.get() == 1:
            buttonsText.set("X")
            playerText.set("Player 2")
            winner = self.checkWin(playerNum.get())
            playerNum.set(2)

        #if button clicked on player 2s turn
        #set button text to X
        #set player turn text to 2 for next turn
        #call check win function, returns the winner, -1 if no winner detected
        #sets player num to 2 for their turn
        elif playerNum.get() == 2:
            buttonsText.set("O")
            playerText.set("Player 1")
            winner = self.checkWin(playerNum.get())
            playerNum.set(1)

        #invalid playernum recieved, 
        else:
            print("Bad player number")

        #if a winner was detected
        #player 1 wins, indicate win and disable all positional buttons
        if winner == 1:
            playerText.set("Player 1 has WON!")
            self.disableAll()
        #player 2 wins, indicate win and disable all positional buttons
        elif winner == 2:
            playerText.set("Player 2 has WON!")
            self.disableAll()

    #diable all positional buttons after a winner detected
    def disableAll(self):
        self.pos00Btn['state'] = 'disabled'
        self.pos10Btn['state'] = 'disabled'
        self.pos20Btn['state'] = 'disabled'
        self.pos01Btn['state'] = 'disabled'
        self.pos11Btn['state'] = 'disabled'
        self.pos21Btn['state'] = 'disabled'
        self.pos02Btn['state'] = 'disabled'
        self.pos12Btn['state'] = 'disabled'
        self.pos22Btn['state'] = 'disabled'

    #reset all button states, user wants to play again
    #set normal state and text
    def resertAll(self):
        self.pos00Btn['state'] = 'normal'
        self.btn_text00.set("")
        self.pos10Btn['state'] = 'normal'
        self.btn_text10.set("")
        self.pos20Btn['state'] = 'normal'
        self.btn_text20.set("")
        self.pos01Btn['state'] = 'normal'
        self.btn_text01.set("")
        self.pos11Btn['state'] = 'normal'
        self.btn_text11.set("")
        self.pos21Btn['state'] = 'normal'
        self.btn_text21.set("")
        self.pos02Btn['state'] = 'normal'
        self.btn_text02.set("")
        self.pos12Btn['state'] = 'normal'
        self.btn_text12.set("")
        self.pos22Btn['state'] = 'normal'
        self.btn_text22.set("")

        #reset player text and num
        self.playerText.set("Player 1")
        self.playerNum.set(1)

    #check win, checks if win condition is met, return winner num
    def checkWin(self, playerNum):

        #init test char and winner (-1 = no winner)
        char = "Y"
        winner = -1

        #find proper char for player
        if playerNum == 1:
            char = "X"
        elif playerNum == 2:
            char = "O"
        else:
            print("Bad player num!")
        
        #test all winning conditions
        #row 1
        if self.btn_text00.get() == char and self.btn_text10.get() == char and self.btn_text20.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #row 2
        elif self.btn_text01.get() == char and self.btn_text11.get() == char and self.btn_text21.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #row 3
        elif self.btn_text02.get() == char and self.btn_text12.get() == char and self.btn_text22.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #column 1
        elif self.btn_text00.get() == char and self.btn_text01.get() == char and self.btn_text02.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #column 2
        elif self.btn_text10.get() == char and self.btn_text11.get() == char and self.btn_text12.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #column 3
        elif self.btn_text20.get() == char and self.btn_text21.get() == char and self.btn_text22.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #cross left to right
        elif self.btn_text00.get() == char and self.btn_text11.get() == char and self.btn_text22.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        #cross right to left
        elif self.btn_text20.get() == char and self.btn_text11.get() == char and self.btn_text02.get() == char:
            print("Winner", playerNum)
            winner = playerNum
        else:
            print("No one has won yet.")

        #return winner number 1,2,-1(no winner)
        return winner

# Create an instance of the MyGUI class.
my_gui = MyGUI()