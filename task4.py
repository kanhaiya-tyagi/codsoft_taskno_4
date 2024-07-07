import random
from tkinter import *

# Create the main window
root = Tk()
root.title("Rock Paper Scissors")

Label(root, text="Rock, Paper, Scissors", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(root, text="Select an option", font=('Calibri', 12)).grid(row=1, sticky=N)

# Setting initial scores to zero
p_scr = 0
c_scr = 0

# Displaying scores
plyr_score = Label(root, text="Player score: ", font=('Calibri', 12))
com_score = Label(root, text="Computer score: ", font=('Calibri', 12))

# Displaying choices and Result
plyr_choice_label = Label(root, font=('Calibri', 12))
com_choice_label = Label(root, font=('Calibri', 12))
outcome = Label(root, font=('Calibri', 20))

# Function for win condition
def win_condition():
    global p_scr
    outcome.config(fg="blue", text="You Win")
    plyr_choice_label.config(fg="green")
    com_choice_label.config(fg="red")
    p_scr += 1
    plyr_score.config(text="Player score: "+ str(p_scr))
    com_score.config(text="Computer score: "+ str(c_scr))

# Function for losing condition
def lose_condition():
    global c_scr
    outcome.config(fg="blue", text="You lose")
    plyr_choice_label.config(fg="red")
    com_choice_label.config(fg="green")
    c_scr += 1
    plyr_score.config(text="Player score: "+ str(p_scr))
    com_score.config(text="Computer score: "+ str(c_scr))

# working of the game
def game_logics(choice):

    psbl_outcms = ["rock", "paper", "scissors"]
    ran  = random.randint(0,2)
    computer_choice = psbl_outcms[ran]

    plyr_choice_label.config(text="Player's Choice : "+ str(choice))
    com_choice_label.config(text="Computer's Choice : "+ str(computer_choice))

    # condition for a tie
    if choice == computer_choice:
        outcome.config(fg="Brown", text="Tie !")
        plyr_choice_label.config(fg="blue")
        com_choice_label.config(fg="blue")

    # Determining the winner or looser
    elif choice == "rock":
        if computer_choice == "paper":
            lose_condition()
        else:
            win_condition()

    elif choice == "paper":
        if computer_choice == "scissors":
            lose_condition()
        else:
            win_condition()

    else:
        if computer_choice == "rock":
            lose_condition()
        else:
            win_condition()

# Resetting the game for next round
def reset():
    outcome.config(text="")
    plyr_choice_label.config(text="")
    com_choice_label.config(text="")
    plyr_score.config(text="Player choice: ")
    com_score.config(text="Computer choice: ")


plyr_score.grid(row=2, sticky=W, padx=50)
com_score.grid(row=2, sticky=E, padx=50)

# Empty label for adding space 
Label(root).grid(row=3)

plyr_choice_label.grid(row=4, sticky=W)
com_choice_label.grid(row=4, sticky=E)
outcome.grid(row=4, sticky=N )

# Empty label for adding space 
Label(root).grid(row=5)

# Buttons for user's choice
Button(root, text="Rock", bg="#d14141", fg="white", width=15, command= lambda: game_logics("rock")).grid(row=6, sticky=W, padx=5, pady=5)
Button(root, text="Paper", bg="#d14141", fg="white", width=15, command= lambda: game_logics("paper")).grid(row=6, sticky=N, padx=5, pady=5)
Button(root, text="Scissors", bg="#d14141", fg="white", width=15, command= lambda: game_logics("scissors")).grid(row=6, sticky=E, padx=5, pady=5)

# Empty label for adding space 
Label(root).grid(row=7)

# Button to reset the game
Button(root, text="Reset", bg="#d1af41",font=("calibri", 14), command= reset ).grid(row=8, sticky=N)
root.mainloop()