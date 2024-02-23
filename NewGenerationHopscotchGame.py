#Nilay
#Import Tkinter and pickle libraries

import tkinter as tk
import pickle

#define function for clicking buttons
def click_button(row, column):
    #define global variables to modify directly
    global current_number, remaining_chances

#conditions for 3 lives
    if remaining_chances==0:
        #Game ends if there is no chance left
        return
    if is_move_valid(row,column):
        current_number+=1
        buttons[row][column].config(text=str(current_number))
        start_label.config(text="Click the button for your next move")
        remaining_chances=3
    else:
        remaining_chances-=1
        if remaining_chances>0:
            start_label.config(text=f"Wrong button! {remaining_chances} chances left!")
        else:
            start_label.config(text=f"Your score is {current_number}. Do you want to play again?")
            add_end_game_buttons()

#define the functions for movement rules
def is_move_valid(row,column):
    global current_number
    #if the clicked button is not empty, move is invalid, 1 chance lost.
    if buttons[row][column].cget("text")!=" ":
        return False
    #if first move, no rules applies
    if current_number==0:
        return True

    prev_row,prev_column=get_prev_position()
    #condition for straight moves (left, right, up or down)
    if row==prev_row or column==prev_column:
        if abs(row-prev_row)==3 or abs(column-prev_column)==3:
            return True
    else:
    #condition for diagonal moves
        if abs(row-prev_row)==2 and abs(column-prev_column)==2:
            return True
    return False

#define a function for positioning
def get_prev_position():
    for i in range(10):
        for j in range(10):
            if buttons[i][j].cget("text")==str(current_number):
                return i,j
    # if the current number is not found, return (-1,-1)
    return -1, -1
#define a func for quitting the game
def quit_game():
    save_game()
    start_label.config(text=f"Your score is {current_number}! See you later!")
    remove_end_game_buttons()
    quit_button.config(state="disabled")
    #to make the game disappear, closing the window
    window.after(2000,window.destroy)

#define a func for Yes, No buttons
def add_end_game_buttons():
    buttons[9][0].config(text="Yes", command=restart_game)
    buttons[9][1].config(text="No", command=quit_game)

# define a func for removing Yes, No buttons
def remove_end_game_buttons():
    buttons[9][0].config(text=" ")
    buttons[9][1].config(text=" ")

#define a func for saving the game
def save_game():
    game_data={"current_number":current_number,
               "remaining_chances":remaining_chances}

    with open("game_state.pkl","wb") as f:
        pickle.dump(game_data, f)

    start_label.config(text="Your game is saved!")
    window.after(2000,lambda :start_label.config(text=" "))

#define a func for restarting the game
def restart_game():
    global current_number, remaining_chances
    for i in range(10):
        for j in range(10):
            buttons[i][j].config(text=" ")
    current_number=0
    remaining_chances=3
    start_label.config(text="NEW GENERATION HOPSCOTCH GAME!\n"
                           "Here are the rules:\n"
                           "1- Start by clicking any button on the board\n"
                           "2- For next move:\n"
                            "a) Hop left, right, up or down by skipping 2 cells\n"
                            "b) Hop diagonal by skipping 1 cell.\n"
                            "3- You have only 3 lives after the wrong move to continue.\n"
                            "4- Your last move would be your score!\n"
                           "Good luck!")
    remove_end_game_buttons()

#create a main window
window=tk.Tk()
start_label=tk.Label(window, text="NEW GENERATION HOPSCOTCH GAME!\n"
                           "Here are the rules:\n"
                           "1- Start by clicking any button on the board\n"
                           "2- For next move:\n"
                            "a) Hop left, right, up or down by skipping 2 cells\n"
                            "b) Hop diagonal by skipping 1 cell.\n"
                            "3- You have only 3 lives after the wrong move to continue.\n"
                            "4- Your last move would be your score!\n"
                           "Good luck!")
start_label.grid(row=0, columnspan=20)
#create a 10X10 grid with clicking buttons
buttons=[]
for i in range(1,11):
    row=[]
    for j in range(10):
        button=tk.Button(window, text=" ", width=2, height=1, command=lambda row=i-1, column=j: click_button(row,column))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

current_number=0
remaining_chances=3

quit_button=tk.Button(window, text="Quit", command=quit_game)
quit_button.grid(row=11, column=0, columnspan=5)

save_button = tk.Button(window, text="Save", command=save_game)
save_button.grid(row=11, column=5, columnspan=2)

#for event loop
window.mainloop()
