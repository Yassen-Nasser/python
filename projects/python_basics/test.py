import random 
import curses

# to initilaize empty screen for starting the game
screen = curses.initscr()

#to prevent the mouse from painting(orange color) on the window
curses.curs_set(0)

# getting thescreen hieght and width
screenHieght, screenWidth= screen.getmaxyx()
#create new window screen by  screenHieght and screenWidth
window  =curses.newwin(screenHieght,screenWidth,0,0)

#to take the inputs from the user from the keyboard
window.keypad(1)
# moving the snake evry 50 milisecond
window.timeout(100)

# the initial position for the head of snake
snk_x = screenWidth//4
snk_y = screenHieght//2

#list that holds the initial(القيمة الاولية) head, body and tail of the snake
snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
]
print(window.getch())