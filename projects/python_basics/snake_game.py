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

#the inital(القيمة الاولية) postion of the food on the screen
food=[screenHieght//2, screenWidth//2 ]

#adding the fisrt food on the screen 
window.addch(food[0], food[1], '@')

# variable holding the initial direction of the snake
key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key
    if snake[0][0] in [0, screenHieght] or snake[0][1] in [0, screenWidth]  or snake[0] in snake[1: ]:
        curses.endwin()
        quit()
         
    new_head= [snake[0][0], snake[0][1]]
    
    if key== curses.KEY_DOWN:
        new_head[0]+= 1  
        
    if key== curses.KEY_UP:
        new_head[0]-= 1
        
    if key== curses.KEY_RIGHT:
        new_head[1]+= 1
    if key== curses.KEY_LEFT:
        new_head[1] -= 1
        
    snake.insert(0, new_head)
    
    if snake[0]==food:
        food = None
        while food is None:
            nf = [
                random.randint(1,screenHieght-1),
                random.randint(1,screenWidth-1)
            ]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], '@')
    else:
        tail = snake.pop()    
        window.addch(tail[0], tail[1], ' ')
        
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
           
 
         