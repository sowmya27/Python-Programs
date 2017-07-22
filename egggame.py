from itertools import cycle
import random
from tkinter import Canvas, Tk, messagebox, font

'''setup canvas'''
canvas_width = 800
canvas_height = 400
root = Tk()# this creates window
root.title("Egg Catcher")
c = Canvas(root,width=canvas_width,height=canvas_height,\
           background = "deep sky blue")
#to create grass
c.create_rectangle(-5,canvas_height-100,canvas_width+5, \
                   canvas_height + 5, fill = "sea green",width=0)
#creates sun for score
c.create_oval(-80,-80,120,120,fill="orange",width=0)
# this function tells the program to draw the main
#window and all its contents
c.pack()
# Run and check now

'''setup eggs'''
#cycle fun from itertools allows you to use each color in turn
color_cycle = cycle(["light blue","light green","light pink",\
                     "light yellow","light cyan"])
egg_width=45
egg_height=55
egg_score=10
egg_speed=500
#time the egg
# Anew egg appears every 4000 milliseconds = 4 sec
egg_interval=4000
#how much the speed and interval change after each catch(closer to 1 is easier)
difficulty_factor = 0.95
'''at end'''

'''set up the catcher'''
catcher_color='blue'
catcher_width = 100
catcher_height=100
#these lines make the catcher start near the
#bottom of the canvas, in the center of the window
catcher_start_x = canvas_width/2 - catcher_width/2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x - catcher_width
catcher_start_y2 = catcher_start_y + catcher_height
#to draw the catcher
catcher = c.create_arc(catcher_start_x, catcher_start_y,\
                       catcher_start_x2,catcher_start_y2,start=200,extent=140,\
                       style ='arc',outline=catcher_color,width=3)

'''score and lives counter'''
game_font=font.nametofont('TkFixedFont')#selects afont
game_font.config(size=18)#change font size

#score
score=0
score_text=c.create_text(10,10,anchor='nw',font=game_font,\
                         fill='darkblue',text='Score:'+str(score))

#lives
lives_remaining = 5
lives_text=c.create_text(canvas_width-10,10,anchor='ne',font=game_font,\
                         fill='darkblue',text='Lives:'+str(lives_remaining))


'''create the eggs'''
eggs=[] #list to keep track of eggs

def create_egg():
    x=random.randrange(10,740)
    y=40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,\
                            fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    #set timer to call the same function again after the given interval or pause
    root.after(egg_interval,create_egg)


'''move eggs'''
def move_eggs():
    #loop through all eggs
    for egg in eggs:
        #to get coordinated of egg
        (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
        #the egg drops down the screen 10 pixels at a time
        c.move(egg,0,10)
        #is the egg bottom of the screen?
        if egg_y2>canvas_height:
            #call function that deals with dropped eggs
            egg_dropped(egg)
    #call this function again to move eggs after mill sec stored in eggspeed
    root.after(egg_speed,move_eggs)


            
''' eggs drop'''
def egg_dropped(egg):
    #remove egg from list
    eggs.remove(egg)
    c.delete(egg)  # egg disappears from canvas
    lose_a_life()
    if lives_remaining ==0:
        messagebox.showinfo('Game Over!','Final Score:'\
                            +str(score))
        root.destroy() #game ends


'''Lose a life'''
def lose_a_life():
    global lives_remaining
    lives_remaining = lives_remaining -1
    #update text that shows the remaining lives
    c.itemconfigure(lives_text,text='Lives:'+str(lives_remaining))


'''check for  a catch'''
def check_catch():
    #get coordinates for catcher
    (catcher_x,catcher_y,catcher_x2,catcher_y2)=c.coords(catcher)
    for egg in eggs:
        #get egg coords
        (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
        #is egg inside the catcher horizontally and vertically
        if catcher_x <egg_x and egg_x2 <catcher_x2 and catcher_y2-egg_y2<40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100,check_catch)


'''increase score'''
def increase_score(points):
    global score,egg_speed, egg_interval
    score = score+ points
    egg_speed= int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    #update text score
    c.itemconfigure(score_text,text="score:"+str(score))

'''set up controls'''
def move_left(event):
    (x1,y1,x2,y2)=c.coords(catcher)
    if x1>0:
        c.move(catcher,-20,0)


def move_right(event):
    (x1,y1,x2,y2)=c.coords(catcher)
    if x2<canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>',move_left)
c.bind('<Right>',move_right)
c.focus_set()

'''start game'''
root.after(1000,create_egg)
root.after(1000,move_eggs)
root.after(1000,check_catch)
root.mainloop()



