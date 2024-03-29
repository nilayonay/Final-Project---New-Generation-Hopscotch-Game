Project Definition: The game is played on a 10X10 grid. The player starts by clicking any button on the grid. It starts with 1 automatically. The aim is to fill out the grid as much as possible according to the rules for the next move. Rules are as follows:
1-	It can go right-left-up-bottom by skipping 2 cells.
2-	It can go diagonally by skipping 1 cell.
3-	There are 3 lives for wrong moves.
4-	The score is the player’s last move.
The player can play the game by clicking buttons, saving the game, resuming the game, quitting the game, or restarting it.

Project Steps and Program Explanation
1-	Creating a 10X10 grid 
a.	Importing libraries: Importing Tkinter for GUI and pickle for saving and loading the game
b.	Creating the main window: window=tk.Tk()
c.	Functions:
click_button(row, column): controls the action when the player clicks the button.
grid() method: creating a board with rows and columns
2-	Starting the game
a.	Creating a label asking the player to “Start by pushing any button”.
b.	Displaying a message to start the game.
c.	Displaying “1” in clicked button.
d.	Starting Thinter event loop. (window.mainloop())
3-	Next move with rules
a.	Defining game and other variables. 
b.	Checking whether the button clicked is adjacent to the previous button clicked (either horizontally, vertically, or diagonally) and updates the current number accordingly.
c.	Functions:
is_move_valid(row, column): checks the conditions according to the rules.
get_prev_position(): finds the row and column of the previous number.
Using loops for checking the conditions and abs for calculating the distance btw two consecutive moves.
4-	Ending game and announcement of the score
a.	Ending the game with no room for movement
b.	Displaying a message with the score
c.	Functions:
add_end_game_buttons(): adds YES, NO and QUIT buttons.
quit_game(): saves the game and closes the window.
save_game(): saves the game, and it stays to continue
remove_end_game_buttons(): clears YES, NO and QUIT buttons if the player clicks YES.
after() method: calls the command with a given period
5-	Saving and resuming game
a.	Asking the player if the player wants to play again
b.	Adding quit and save buttons.
c.	Functions:
add_end_game_buttons(): adds YES, NO and QUIT buttons.
quit_game(): saves the game and closes the window.
remove_end_game_buttons(): clears YES, NO and QUIT buttons if the player clicks YES.
save_game(): saves the situation to a file and prints the “Your game is saved!” message

