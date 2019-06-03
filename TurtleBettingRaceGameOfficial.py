###---------------  TURTLE BETTING RACE GAME -------------------###
###--------------- BY VINAY KUMAR SHUKLA --------------- ###

#IMPORTING MODULES 
from tkinter import *
import time
from turtle import *
from random import randint
import math
from tkinter import messagebox

#IT WILL CREATE THE BACKGROUND WHERE THE GAME WILL BE DISPLAY.
def playbg(s): # STRING s CONTAINS THE NAME OF THE COLOR TO BE PAINTED 
    g1=Turtle()
    g1.penup()
    g1.goto(-400,400)
    g1.begin_fill()
    g1.color(s)
    g1.forward(800)
    g1.right(90)
    g1.forward(800)
    g1.right(90)
    g1.forward(800)
    g1.right(90)
    g1.forward(800)
    g1.end_fill()

#MONEY GAME CODE    
def earnmoney():
            #setting up screen
    global score
    wn=Screen()
    wn.bgcolor("light green")

    playbg("light green")

    #information
    info=Turtle()
    info.penup()
    info.goto(-380,50)
    info.write("Press d for return\nto main game\nin Day mode")
    info.goto(-380,-50)
    info.write("Press n for return\nto main game\nin Night mode")
    

               #Draw border
    mypen=Turtle()
    mypen.penup()
    mypen.setposition(-290,-310)
    mypen.pendown()
    mypen.pensize(5)
    for side in range(4):
        mypen.forward(600)
        mypen.left(90)
    
    #POINTS TABLE
    point=Turtle()
    point.penup()
    point.goto(-380,250)
    point.hideturtle()
    def points():
        point.write("SCORE\n",font=("ARIAL",15,"bold"))
        point.write(score,font=("ARIAL",15,"bold"))
        
    
    #Creating player
    player=Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)

    #Create goals
    goals=[]
    maxGoals=6
    for count in range(maxGoals):
        goals.append(Turtle())
        goals[count].color("red")
        goals[count].shape("circle")
        goals[count].penup()
        goals[count].speed(0)
        goals[count].setposition(randint(-300,300),randint(-300,300))

    
    #define functions
    def turnleft():
        player.left(30)
    def turnright():
        player.right(30)
    def increasespeed():
        global s
        s+=1
    def decreasespeed():
        global s
        s-=1
        
    #IT WILL CHECK THE COLLISION BETWEEN PLAYER ANDE RED BALL
    def isCollision(t1,t2):
        d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if d<20:
            return True
        else:
            return False
        
                
    #set keyboard bindings
    listen()
    onkey(turnleft,"Left")
    onkey(turnright,"Right")
    onkey(increasespeed,"Up")
    onkey(decreasespeed,"Down")
    onkey(daybackground,"d")
    onkey(nightbackground,"n")

    points()

    while True:
        player.forward(s)

        #Boundary Checking
        if player.xcor()>290 or player.xcor()<-290:
            player.right(180)
        if player.ycor()>290 or player.ycor()<-290:
            player.right(180)

#MOVING THE BALLS WITH CONSTANT SPEED
        for count in range(maxGoals):
            goals[count].forward(5)
            
         #iF COLLISION IS OCCURED, IT WILL CHANGFE THE BALL POSIOTION AND UPDATES THE POINTS   
            if isCollision(player,goals[count]):
                goals[count].setposition(randint(-290,310),randint(-290,310))
                goals[count].right(randint(0,360))
                score+=10
                point.undo()
                points()
                    

            if goals[count].xcor()>280 or goals[count].xcor()<-280:
                goals[count].right(180)

            if goals[count].ycor()>280 or goals[count].ycor()<-280:
                goals[count].right(180)
    
#IN NIGHT MODE, IT WILL DREAW THE MOUNTAINS                 
def mount():
    mountain=Turtle()
    mountain.begin_fill()
    mountain.fillcolor("darkslategrey")
    mountain.goto(-100,0)
    mountain.left(45)
    mountain.forward(200)
    mountain.right(90)
    mountain.forward(200)
    mountain.left(45)
    mountain.left(45)
    mountain.forward(200)
    mountain.right(90)
    mountain.forward(200)
    mountain.end_fill()
    mountain.hideturtle()

#IT WILL DRAW THE BOX OF WALLET
def square():
    sq=Turtle()
    sq.penup()
    sq.goto(-380,-250)
    sq.begin_fill()
    sq.pendown()
    sq.fillcolor("LIME")
    sq.forward(130)
    sq.right(90)
    sq.forward(50)
    sq.right(90)
    sq.forward(130)
    sq.right(90)
    sq.forward(50)
    sq.end_fill()
    sq.hideturtle()

#SHOW THE MONEY STATUS AND DEDUCT OR CREDIT THE MONEY 
def money():
    global amount
    global score
    amount+=score
    score=0
    square()
    money=Turtle()
    money.penup()
    money.goto(-370,-290)
    
    #condition for deducting and crediting money 
    if(bet==0):
        amount-=betmoney
    elif(bet==1):
        if(plno==2):
            amount+=betmoney
        elif(plno==3):
            amount += (betmoney*2)
        elif(plno==4):
            amount+=(betmoney*3)
        else:
            amount+=(betmoney*4)
    else:
        pass
    
    money.write("Money you have\n",font=("ARIAL",10,"bold"))
    money.write(amount,font=("ARIAL",10,"bold"))
    money.hideturtle()

#SHOW THE MESSAGE FOR NOT HAVING ENOUGH MONEY AND GO TO EARNING MONEY GAME
    if amount<10:
        zero=Turtle()
        zero.penup()
        zero.pencolor("red")
        zero.goto(-100,50)
        zero.begin_fill()
        zero.fillcolor("lime")
        zero.forward(320)
        zero.right(90)
        zero.forward(120)
        zero.right(90)
        zero.forward(320)
        zero.right(90)
        zero.forward(120)
        zero.right(90)
        zero.end_fill()
        zero.goto(-90,-60)
        zero.write("YOU HAVE LOW MONEY\nTO PLAY THE GAME\nPRESS e TO EARN MONEY",font=("ARIAL",18,"bold"))
        listen()
        onkey(earnmoney,"e")
        
        
#IT WILL CREATE THE GROND FOR RACING
#CREATES THE FINISHING LINE
def ground(col1):
    global bet
    global betmoney
    g=Turtle()
    g.color("black")
    g.begin_fill()
    g.fillcolor(col1)
    g.goto(-400,0)
    g.penup()
    g.forward(800)
    g.right(90)
    g.forward(320)
    g.right(90)
    g.forward(800)
    g.right(90)
    g.forward(320)
    g.end_fill()
    g.hideturtle()
    
    #FINISH LINE
    finish=Turtle()
    stamp_size=20
    square_size=15
    finish_line=200
    finish.color("black")
    finish.shape("square")
    finish.shapesize(square_size/stamp_size)
    finish.penup()

    for i in range(10):
        finish.setpos(finish_line,(-10-(i*square_size*2)))
        finish.stamp()
    for j in range(10):
        finish.setpos(finish_line+square_size,((-10-square_size)-(j*square_size*2)))
        finish.stamp()
    finish.hideturtle()

    #MONEY BOX
    bet=10
    betmoney=10
    money()


#DRAW ONE STAR
def drawstar():
    turns=5
    star.begin_fill()
    while turns>0:
        star.forward(10)
        star.left(145)
        turns-=1
    star.end_fill()

#IT WILL  CREATE THE NIGHT BACKGROUND GUI    
def nightbackground():
    global flag
    global plsnameflag

    #LOAD THE TEXT BEFORE GAME IS LOADING.
    text.penup()
    text.goto(-200,50)
    text.color("purple")
    text.write("LOADING THE GAME ......\nPLEASE WAIT",font=("ARIAL",30,"bold"))
    text.hideturtle()

    #IT WILL LOAD THE MOON IMAGE ON THE SCREEN
    playbg("black") 
    screen.bgcolor("black")
    img="C:/Users/Vinay/AppData/Local/Programs/Python/Python37-32/moon.gif"
    screen.addshape(img)
    moon=Turtle()
    moon.shape(img)
    moon.penup()
    moon.goto(-280,200)

    #IT WILL DRAW STARS
    star.color("white")
    star.speed(0)
    num_stars=0
    while num_stars<50:
        x=randint(-200,350)
        y=randint(20,300)
        drawstar()
        star.penup()
        star.goto(x,y)
        star.pendown()
        num_stars+=1
    star.hideturtle()
    
    #CALLING MountaiN FOUNCTION
    mount()

    maingame("grey")

    #SHOWING MESSAGE
    #AND RESTART THE GAME WHEN ENTER IS PRESSED
    #AND TAKE EXIT WHEN ESCAPE IS PRESSED
    repeat1=Turtle()
    while(1):

        
        repeat1.color("red")
        repeat1.penup()
        repeat1.goto(-150,250)
        repeat1.pendown()
        repeat1.write("PRESS ENTER, TO PLAY AGAIN\nOR\nPRESS ESC, TO EXIT",font=("ARIAL",10,"bold"))
        onkey(lambda:maingame("grey"),"Return")
        listen()
        onkey(bye,"Escape")
        listen()
    repeat1.hideturtle()

#IT WILL CREATE THE DAY BACKGROUND
def daybackground():
    global flag
    global plsnameflag

    #Loading text
    text.penup()
    text.goto(-200,50)
    text.color("BLUE")
    text.write("LOADING THE GAME ........\nPLEASE WAIT",font=("ARIAL",30,"bold"))
    text.hideturtle()

    #Creating game arena sky
    playbg("dodgerblue")
    
    #screen color changing           
    screen.bgcolor("dodgerblue")
    
    #creating plants and tress
    t=Turtle()
    t.speed(0)
    t.begin_fill()
    t.fillcolor("forestgreen")
    t.forward(350)
    t.backward(350)
    t.left(90)
    t.forward(5)
    t.circle(-10,180)
    t.left(180)
    t.circle(-10,180)
    t.left(200)
    t.forward(10)
    t.circle(-40,240)
    t.end_fill()
    t.begin_fill()
    t.penup()
    t.goto(100,60)
    t.pendown()
    t.left(220)
    t.forward(200)
    t.circle(-80,180)
    t.forward(260)
    t.left(180)
    t.circle(-30,180)
    t.left(180)
    t.circle(-50,180)
    t.end_fill()
    t.hideturtle()
#sun
    
    sun=Turtle()
    sun.penup()
    sun.goto(-300,150)
    sun.pendown()
    sun.speed(0)
    sun.color('red')
    sun.begin_fill()
    for i in range(50):
        sun.forward(200)
        sun.left(170)
        sun.fillcolor("yellow")
    sun.end_fill()
    sun.hideturtle()

#CALLING MAINGAME FUNCTION
    maingame("chocolate")

#SHOWING MESSAGE
#AND RESTART GAME IF ENTER KEY PRESSED
#AND EXIT IS ESCAPE IS PRESSED
    repeat=Turtle()
    while(1):
        repeat.penup()
        repeat.goto(-150,250)
        repeat.pendown()
        repeat.write("PRESS ENTER, TO PLAY AGAIN\nOR\nPRESS ESC, TO EXIT",font=("ARIAL",10,"bold"))
        onkey(lambda:maingame("chocolate"),"Return")
        onkey(lambda: bye(),"Escape")
        listen()
    repeat.hideturtle()
    
#IT WILL TAKE THE BETTING MONEY AND BETTING PLAYER NAME INPUT FROM USER
def userin():
    #turtleforbet
    global betmoney
    global betturtle
    global betturt
    betmoney=numinput("Betting Money","Enter the amount for betting",minval=10,maxval=amount)
    betturtle=textinput("Bet Turtle Name","Enter the Name of the Turtle You want to put Bet")
    
    #CONVERTING THE INPUT TO UPPERCASE 
    betturt=betturtle.upper()

    #sHOWING MESSAGE IF THE NAME OF THE BETTING PLAYER DOESN'T MATCH ANY PLAYUER NAME
    if((betturt!=p1) and (betturt!=p2) and (betturt!=p3) and (betturt !=p4) and (betturt!=p5)):
        messagebox.showinfo("Wrong Turtle Name","The Turtle Name you Entered\nDoesn't match with any\nPlayer name")
        userin()

#THIS FUNCTION WILL INTEGRATE ALL THE FUNCTION TO IMPLEMENT THE FUNCTIONING OF THE GAME
def maingame(col):

    global betturt
    global betmoney
    global bet
    global p1
    global p2
    global p3
    global p4
    global p5
    global plno

    #CALLING GROUND FUNCTION
    ground(col)

    #Taking the Input from user for deciding no. of players in game 
    plno=numinput("NUMBER OF PLAYERS","ENTER THE NUMBER OF PLAYERS\nYOU WANT IN THE GAME",minval=2,maxval=5)

    #SUPPLYING DEFAULT NAMES AND COLORS TO PLAYERS USING DICTIONARY
    pldict={'red':'BEN','green':'GWEN','blue':'GOKU','yellow':'GOHAN','pink':'MISTY'}

    #ASKING IF USER WANTS TO ENTER PLAYERS NAME
    plnames=textinput("NAME OF PLAYERS","ENTER YES IF YOU WANT\nTO ENTER PLAYERS NAME")
    no=1
    
    plnamesdecision=plnames.upper()
    if(plnamesdecision=="YES" or plnamesdecision=="Y"):
        for i,j in pldict.items():
            if(no<=plno):
                pldict[i]=textinput("PLAYER NAME","ENTER PLAYER "+str(no)+" NAME : ")
                no+=1
    else:
        pass

    #CONVERTING THEIR NAME TO UPPERCASE 
    p1=pldict['red'].upper()
    p2=pldict['green'].upper()
    p3=pldict['blue'].upper()
    p4=pldict['yellow'].upper()
    p5=pldict['pink'].upper()

    turtle1=Turtle()
    turtle2=Turtle()
    turtle3=Turtle()
    turtle4=Turtle()
    turtle5=Turtle()
    name=Turtle()

    name.penup()

    #Putting players name in screen
    if(plno==2):
        name.goto(-250,-100)
        name.write(p1,font=("ARIAL",10,"bold"))

        name.goto(-250,-150)
        name.write(p2,font=("ARIAL",10,"bold"))
    
        turtle1.penup()
        turtle1.color('red')
        turtle1.shape('turtle')
        turtle1.penup()
        turtle1.goto(-250,-100)
        turtle1.pendown()

        turtle2.penup()
        turtle2.color('green')
        turtle2.shape('turtle')
        turtle2.penup()
        turtle2.goto(-250,-150)
        turtle2.pendown()

    if(plno==3):
        name.goto(-250,-100)
        name.write(p1,font=("ARIAL",10,"bold"))

        name.goto   (-250,-150)
        name.write(p2,font=("ARIAL",10,"bold"))

        name.goto(-250,-200)
        name.write(p3,font=("ARIAL",10,"bold"))
    
    
        turtle1.penup()
        turtle1.color('red')
        turtle1.shape('turtle')
        turtle1.penup()
        turtle1.goto(-250,-100)
        turtle1.pendown()

        turtle2.penup()
        turtle2.color('green')
        turtle2.shape('turtle')
        turtle2.penup()
        turtle2.goto(-250,-150)
        turtle2.pendown()
    
        turtle3.penup()
        turtle3.color('blue')
        turtle3.shape('turtle')
        turtle3.penup()
        turtle3.goto(-250,-200)
        turtle3.pendown()

    if(plno==4):
        name.goto(-250,-100)
        name.write(p1,font=("ARIAL",10,"bold"))

        name.goto(-250,-150)
        name.write(p2,font=("ARIAL",10,"bold"))

        name.goto(-250,-200)
        name.write(p3,font=("ARIAL",10,"bold"))

        name.goto(-250,-250)
        name.write(p4,font=("ARIAL",10,"bold"))

        turtle1.penup()
        turtle1.color('red')
        turtle1.shape('turtle')
        turtle1.penup()
        turtle1.goto(-250,-100)
        turtle1.pendown()

        turtle2.penup()
        turtle2.color('green')
        turtle2.shape('turtle')
        turtle2.penup()
        turtle2.goto(-250,-150)
        turtle2.pendown()
        
        turtle3.penup()
        turtle3.color('blue')
        turtle3.shape('turtle')
        turtle3.penup()
        turtle3.goto(-250,-200)
        turtle3.pendown()

        turtle4.penup()
        turtle4.color('yellow')
        turtle4.shape('turtle')
        turtle4.penup()
        turtle4.goto(-250,-250)
        turtle4.pendown()
    if(plno==5):
    
        name.goto(-250,-100)
        name.write(p1,font=("ARIAL",10,"bold"))

        name.goto(-250,-150)
        name.write(p2,font=("ARIAL",10,"bold"))

        name.goto(-250,-200)
        name.write(p3,font=("ARIAL",10,"bold"))

        name.goto(-250,-250)
        name.write(p4,font=("ARIAL",10,"bold"))

        name.goto(-250,-300)
        name.write(p5,font=("ARIAL",10,"bold"))
                   
        turtle1.penup()
        turtle1.color('red')
        turtle1.shape('turtle')
        turtle1.penup()
        turtle1.goto(-250,-100)
        turtle1.pendown()

        turtle2.penup()
        turtle2.color('green')
        turtle2.shape('turtle')
        turtle2.penup()
        turtle2.goto(-250,-150)
        turtle2.pendown()
        
        turtle3.penup()
        turtle3.color('blue')
        turtle3.shape('turtle')
        turtle3.penup()
        turtle3.goto(-250,-200)
        turtle3.pendown()

        turtle4.penup()
        turtle4.color('yellow')
        turtle4.shape('turtle')
        turtle4.penup()
        turtle4.goto(-250,-250)
        turtle4.pendown()
        
        turtle5.penup()
        turtle5.color('pink')
        turtle5.shape('turtle')
        turtle5.penup()
        turtle5.goto(-250,-300)
        turtle5.pendown()



     #Taking bet money and turtle name for bet
    userin()
        
#RaceLight
    plname=Turtle()
    light=Turtle()
    light.penup()
    light.hideturtle()
    light.goto(-200,-50)
    light.begin_fill()
    light.fillcolor("red")
    light.circle(20)
    light.end_fill()
    plname.penup()
    plname.color("black")
    plname.goto(-280,-20)
    plname.pendown()
    plname.write("Ready",font=("ARIAL",10,"bold"))
    time.sleep(3)
    light.begin_fill()
    light.color("yellow")
    light.circle(20)
    light.end_fill()
    plname.penup()
    plname.goto(-280,-35)
    plname.pendown()
    plname.write("Steady",font=("ARIAL",10,"bold"))
    time.sleep(2)
    light.begin_fill()
    light.color("green")
    light.circle(20)
    light.end_fill()
    plname.penup()
    plname.goto(-280,-50)
    plname.pendown()
    plname.write("GO",font=("ARIAL",10,"bold"))

    light.hideturtle()
    plname.hideturtle()

    turtle1.penup()
    turtle2.penup()
    turtle3.penup()
    turtle4.penup()
    turtle5.penup()

    #START RACING
    for i in range(85):
        if(plno==2):
            turtle1.forward(randint(1,10))
            turtle2.forward(randint(1,10))
        if(plno==3):
            turtle1.forward(randint(1,10))
            turtle2.forward(randint(1,10))
            turtle3.forward(randint(1,10))
        if(plno==4):
            turtle1.forward(randint(1,10))
            turtle2.forward(randint(1,10))
            turtle3.forward(randint(1,10))
            turtle4.forward(randint(1,10))                
        if(plno==5):
            turtle1.forward(randint(1,10))
            turtle2.forward(randint(1,10))
            turtle3.forward(randint(1,10))
            turtle4.forward(randint(1,10))
            turtle5.forward(randint(1,10))


    #OBTAINING FINAL POSITIONS OF TURTLES
    pos1=turtle1.position()
    pos2=turtle2.position()
    pos3=turtle3.position()
    pos4=turtle4.position()
    pos5=turtle5.position()
    
    winner=Turtle()
    winner.hideturtle()
    winner.color("white")
    bet=0
    posdict=[1,2,3,4,5]
    posdict[0]=pos1
    posdict[1]=pos2
    posdict[2]=pos3
    posdict[3]=pos4
    posdict[4]=pos5

    lengthofpos=len(posdict)
    max=0
    
    #DETERMINIUNG THE WINNER PLAYER POSITION
    for i in range(lengthofpos):
        if(posdict[i]>posdict[max]):
            max=i
            
    #DETERMINING THE WINNER NAME AND PUTTING IT ON THE SCREEN 
    if(posdict[max]==pos1):
        winner.penup()
        winner.goto(-100,-100)
        winner.write(p1,font=("ARIAL",50,"bold"))
        winner.penup()
        winner.goto(-280,-200)
        winner.pendown()
        winner.write("WON THE RACE",font=("ARIAL",50,"bold"))

        #CHECKING WHETHER USER WON THE BET
        if(betturt==p1):
            bet=1

    if(posdict[max]==pos2):
        winner.penup()
        winner.goto(-100,-100)
        winner.write(p2,font=("ARIAL",50,"bold"))
        winner.penup()
        winner.goto(-280,-200)
        winner.pendown()
        winner.write("WON THE RACE",font=("ARIAL",50,"bold"))
        if(betturt==p2):
            bet=1
    if(posdict[max]==pos3):
        winner.penup()
        winner.goto(-100,-100)
        winner.write(p3,font=("ARIAL",50,"bold"))
        winner.penup()
        winner.goto(-280,-200)
        winner.pendown()
        winner.write("WON THE RACE",font=("ARIAL",50,"bold"))
        if(betturt==p3):
            bet=1
    if(posdict[max]==pos4):
        winner.penup()
        winner.goto(-100,-100)
        winner.write(p4,font=("ARIAL",50,"bold"))
        winner.penup()
        winner.goto(-280,-200)
        winner.pendown()
        winner.write("WON THE RACE",font=("ARIAL",50,"bold"))
        if(betturt==p4):
            bet=1
    if(posdict[max]==pos5):
        winner.penup()
        winner.goto(-100,-100)
        winner.write(p5,font=("ARIAL",50,"bold"))
        winner.penup()
        winner.goto(-280,-200)
        winner.pendown()
        winner.write("WON THE RACE",font=("ARIAL",50,"bold"))
        if(betturt==p5):
            bet=1
    #SHOWING THE MESSAGE WHETHER USER WON THE BET OR NO
    if(bet==1):
        messagebox.showinfo("BETTING RESULT","YOU WON THE BET")
    elif(bet==0):
        messagebox.showinfo("BETTING RESULT","YOU LOOSE THE BET")
    else:
        pass
    #CALLING MONEY FUNCTION
    money()
    

   
#THIS FUNCTION WILL SHOW MODES BUTTON 
def start():
    
    l2=Label(fm,text="Choose the game mode")
    l2.place(x=20,y=120)
    l2.config(font=("ARIAL",10,"italic"),background="white")
    mod1=Button(fm,command=daybackground,text="Day Mode")
    mod1.config(width=30)
    mod1.place(x=0,y=150)
    mod2=Button(fm,command=nightbackground,text="Night Mode")
    mod2.config(width=30)
    mod2.place(x=0,y=170)

#set speed variable
s=1
title("TURTLE BETTING RANDOM RACE GAME")
text=Turtle()
star=Turtle()
screen=Screen()
flag=None
plsnameflag=None
p1=None
p2=None
p3=None
p4=None
p5=None
betturtle=None
betturt=None
score=0
bet=10
betmoney=10

#WALLET MONEY 
amount=10000

#IT WILL SHOW THE MENU
root=Tk()
root.title("TURTLE BETTING RACE GAME")

fm=Frame(root,bg="red") 
fm.place(height=200,width=200,x=0,y=0)
x=Label(fm,text="WELCOME TO TURTLE RACE ")
x.config(font=("ARIAL",10,"italic"),background="yellow")
x.pack()
b=Button(fm,command=start,text="Start the game")
b.config(width=30)
b.place(x=0,y=80)
root.mainloop()
    

########--------------------------            END OF THE PROGRAM             -----------------------###############

