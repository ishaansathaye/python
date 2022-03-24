#Friday, July 17, 2015 at 7:21 PM
from tkinter import *
import random

# use a class definition to hold all my functions
class MyApp(Tk):
    def __init__(self):
        """ initialize the frame and widgets"""
        #load Tk
        Tk.__init__(self)

        #make a frame
        fr = Frame(self)

        #intialize operation buttons and the label
        self.player_button = Button(self, text="Me",
                                    command=lambda: self.do_start(TRUE),
                                    font=("Helvetica", 16))
        self.computer_button = Button(self, text="Computer",
                                      command=lambda: self.do_start(FALSE),
                                      font=("Helvetica", 16))
        self.exit_button = Button(self, text="Exit", command=self.do_exit,
                                  font=("Helvetica", 16))
        self.again_button = Button(self, text="again?", command=self.do_again,
                                   state=DISABLED,
                                   font=("Helvetica", 16))
        self.myLabel = Label(self, text="Who starts?", font=("Helvetica", 16))

        #initialize a list to use for my field buttons (note: 0 is not used)
        self.bList = [0,1,2,3,4,5,6,7,8,9]

        #use a loop to build my field buttons
        for i in range(1,10):
            self.bList[i] = Button(self, text="---",  #bList now button references
                                   command=lambda j=i: self.do_button(j),
                                   state=DISABLED, relief=RAISED, height=3,
                                   width=7, font=("Helvetica", 24))

        #grid everything into the frame
        fr.grid()
        self.myLabel.grid(row=0, columnspan=4)
        self.player_button.grid(row=1, column=0)
        self.computer_button.grid(row=1, column=2)
        self.exit_button.grid(row=5, column=0)
        self.again_button.grid(row=5, column=2)

        #use a loop to grid the field buttons
        myL = [[1,4,0], [2,4,1], [3,4,2],  #button number, row, column
               [4,3,0], [5,3,1], [6,3,2],
               [7,2,0], [8,2,1], [9,2,2]]
        for i in myL:
            self.bList[i[0]].grid(row=i[1], column=i[2])

    def do_start(self,player):
        """start the game, if player is TRUE, player make first move"""
        #turn Me, computer, and again? buttons off
        self.player_button.config(state=DISABLED)
        self.computer_button.config(state=DISABLED)
        self.again_button.config(state=DISABLED)

        #reset the bState and mySums lists and the flags
        self.bState = [10,0,0,0,0,0,0,0,0,0]  #state of button 1-player -1-comp 0-open
        self.mySums = [0,0,0,0,0,0,0,0]       #sums of rows, columns and diagonals
        self.gameDone = FALSE
        self.specialDefense = FALSE

        #turn the field buttons on
        for i in range(1,10):
            self.bList[i].config(state=NORMAL)

         #if player is true the player starts otherwise the computer starts
        self.myLabel.config(text="You are X, make a move")
        if player:
            self.turn = FALSE
        else:
            self.turn = TRUE
            self.do_move()

    def do_button(self, i):
        """handle a field button click"""
        #i is the number of the button that was pushed note: 1 through 9
        # if turn is true the computer made a move otherwie player
        if self.turn:
            myText = "-0-"
            self.turn = FALSE
            self.bState[i] = -1
        else:
            myText = "-X-"
            self.turn = TRUE
            self.bState[i] = 1

        #Disable the ith button and test if we are done
        self.bList[i].config(text=myText, state=DISABLED)
        self.test_done()

        # if it is the computer's turn and the game is not over make a move
        if (self.turn) and (not self.gameDone):
            self.do_move()

    def test_done(self):
        """test if the game is over"""
        #if there is not a 0 in bstate the game is done
        if not (0 in self.bState):
            self.myLabel.config(text="Draw, game over!")
            self.gameDone = TRUE
            self.again_button.config(state=NORMAL)

        #after doing sums look for 3 or -3 to find if there was a winner
        self.do_sums()
        if 3 in self.mySums: #note 3 in mySums means player has won
            self.myLabel.config(text="You won!")
            self.gameDone = TRUE
            self.again_button.config(state=NORMAL)
        elif -3 in self.mySums: #note -3 in mySums means computer has won
            self.myLabel.config(text="Computer won!")
            self.gameDone = TRUE
            self.again_button.config(state=NORMAL)

    def do_sums(self):
        """put a list of the various row, column, and diagonal sums in mySums"""
        triples = [[1,2,3], [4,5,6], [7,8,9], #rows
                   [1,4,7], [2,5,8], [3,6,9], #columns
                   [1,5,9], [3,5,7]]          #diagonals
        count = 0
        for i in triples:
            self.mySums[count] = 0
            for j in i:
                self.mySums[count] += self.bState[j]

            count += 1

    def do_move(self):
        """computer picks a move to make"""
        #mix it up a little by starting with the center for first move sometimes
        if (not 1 in self.bState) and (not -1 in self.bState): #i.e. first move
            if random.random() < 0.20:   #20% of the time start in center
                self.do_button(5)
                return

        #handle the case where player as made first move to a corner
        if (1 in self.bState) and (not -1 in self.bState):
            if self.bState.index(1) in [1,3,7,9]:
                self.do_button(5)
                self.specialDefense = TRUE
                return

        #test if computer can win, if so do the move
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = -1   #make a trial move
                self.do_sums()
                if -3 in self.mySums: #note -3 means computer has won
                    self.do_button(i) #make move if a win
                    return
                else:
                    self.bState[i] = 0 #switch back of not a win

        #test if player can win, if so block
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = 1   #make a trial move
                self.do_sums()
                if 3 in self.mySums: #note 3 in bState means player has won
                    self.do_button(i) #block if player could win
                    self.specialDefense = FALSE #special defense no longer needed
                    return
                else:
                    self.bState[i] = 0 #switch back of not a win

        #for the second special defense move, pick a side (if not already done)
        if self.specialDefense:
            self.specialDefense = FALSE
            sides = [2,4,6,8]
            random.shuffle(sides)  #shuffle them so people don't get as bored
            for i in sides:
                if self.bState[i] == 0:
                    self.do_button(i)
                    return

        #pick a corner if open
        corners = [1,3,7,9]
        random.shuffle(corners)   #shuffle them so people don't get as bored
        for i in corners:
            if self.bState[i] == 0:
                self.do_button(i)
                return

        #take center if open
        if self.bState[5] == 0:
            self.do_button(5)
            return

        #pick a side if open
        sides = [2,4,6,8]
        random.shuffle(sides)  #shuffle them so people don't get as bored
        for i in sides:
            if self.bState[i] == 0:
                self.do_button(i)
                return

    def do_again(self):
        """reset everything to play again"""
        #reset my buttons and change the label
        self.player_button.config(state=NORMAL)
        self.computer_button.config(state=NORMAL)
        self.myLabel.config(text="Who starts?")

        #disable the field buttons
        for i in range(1,10):
            self.bList[i].config(text="---", state=DISABLED)

    def do_exit(self):
        """destroy the frame when exit is pushed"""
        root.destroy()
# end of MyApp class

if __name__ == '__main__':
    root = MyApp()
    root.title("Tic Tac Toe")
    root.mainloop()
