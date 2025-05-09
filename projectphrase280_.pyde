add_library('minim')
def setup():
    global stage,title,bg,monsterA,visible,player,over,rectwidth,excit,restart,left#this is for storing different varible
    global death,right,attack,stand,player1,player2,player3,player4,player5,player6,a,monsterx,monstery,monsterdx,monsterdy,monster,monster2
    global x, y,player7,player8,starttime,b, delay,health
    global minim,punch,score,hurt,record1,fireball, manymonster,manymonsterx,manymonstery
    global manymonsterdx,bg2,alive,enemyhealth,warning,stage2attack,baldattack
    global wizard,wizardattack,furthertime,wizardx,wizardy,wizardlife,wizardexist
    global medkit,restore,increase,stage2time,sound,sounddelay,magicattack,fireballx,firebally
    global bg3,fireballimg,record3,record2,melee,meleepic,finalrecord,ball,ballcontrol
    global hankhealth,hankattack,hankattack2,hankxposition,hankmmoveright,hankmoveleft,hanktime
    global hankdelay,rock,scissor,paper,robot,playeroption,win,lose,winwin,strength
    global plane, planebullet,enemyplane,enemybullet,hank,hankalive,hankx,hanky
    global hankpunch,hankrush,bullettotalnum,hank,sky,pos,speed,playerplanex
    global playerplaney,enemyplaney,enemyplanex,playerplanex
    global enemyplanehealth,enemyplanespeed,playerplanespeed
    global playerbulletx,playerbullety,enemybulletx,enemybullety
    global playerbulletvisible,enemybulletvisible,bulletspeed
    global planespeed,bulletdelay,bullettime,last1,last2,last3,dial3
    global dial4,bg5,chocosleep,bg6,chocosad,lobby,outside,choco,good
    global happy,hotel
    hotel=loadImage("hotel.jpg")
    happy=loadImage("happy.jpg")
    good=loadImage("congrats.PNG")
    choco=loadImage("choco1.png")
    lobby=loadImage("lobby.jpg")
    outside=loadImage("outside.jpg")
    chocosad=loadImage("choco3.png")
    bg6=loadImage("bg6.jpg")
    chocosleep=loadImage("choco2.png")
    bg5=loadImage("bg5.jpg")
    dial3=0
    dial4=0
    last3=0
    last2=0
    last1=0
    bullettime=millis()
    bulletdelay=3000
    planespeed=2
    bulletspeed=5
    enemybullet=loadImage("bullet3.png")
    planebullet=loadImage("bullet1.png")
    playerbulletvisible=[]
    enemybulletvisible=[]
    playerbulletx=[]
    playerbullety=[]
    enemybulletx=[]
    enemybullety=[]
    enemyplanespeed=5
    playerplanespeed=5
    enemyplanehealth=0
    playerplanex=400
    playerplaney=700
    enemyplanex=400
    enemyplaney=100
    pos=0
    speed=-0.2
    sky=loadImage("sky.jpg")
    plane=loadImage("playerplane1.png")
    enemyplane=loadImage("hankplane1.png")
    bullettotalnum=30
    hankrush=0
    hankpunch=0
    hankx=600
    hanky=400
    hank=loadImage("boss0.png")
    strength=1
    winwin=loadImage("draw.png")
    win=loadImage("win.png")
    lose=loadImage("lose.jpg")
    playeroption=0
    robot=0
    rock=loadImage("rock.png")
    scissor=loadImage("scissor.png")
    paper=loadImage("paper.png")    
    hankalive=True
    hanktime=millis() 
    hankhealth=0
    hankattack=[]
    hankattack2=[]
    hankmove=loadImage("boss10.png")
    ballcontrol=True
    ball=[]
    finalrecord=0
    meleepic=0
    melee=[]
    record2=0
    record3=0
    fireballimg=loadImage("fireball.png")
    fireballx=[]
    firebally=[]
    bg3=loadImage("bg3.jpg")
    magicattack=millis()
    sounddelay=10000
    sound=millis()
    stage2time=[]
    increase=10
    restore=False
    medkit=3
    wizardlife=0
    wizardexist=True
    wizardx=100
    wizardy=400
    furthertime=3000
    wizardattack=loadImage("wizard4.png")
    wizard=loadImage("wizard0.png")
    baldattack=[]
    stage2attack=[]
    enemyhealth=[]
    alive=[]
    bg2=loadImage("bg2.png")
    manymonster=loadImage("enemy0.png")
    manymonsterx=[]
    manymonstery=400
    manymonsterdx=[]
    fireball=[]
    score=0
    record1=0
    minim=Minim(this)
    punch=minim.loadFile("punch.wav")#storeing different voice for attack voice
    warning=minim.loadFile("warning.mp3")
    hurt=minim.loadFile("punch.wav")
    delay=3000
    b=2
    health=0
    starttime=millis()
    size(800,800)
    monsterx=500
    monster=[]
    monster2=loadImage("monster2.png")
    monstery=450
    stage=0
    monsterdx=0
    a=0
    left=False
    right=False
    attack=False
    stand=True
    player1=loadImage("player1.png")#storing players different action
    player2=loadImage("player2.png")
    player3=loadImage("player3.png")
    player4=loadImage("player4.png")
    player5=loadImage("player5.png")
    player6=loadImage("player6.png")
    player7=[]
    player8=loadImage("player7.png")
    x=100
    y=400
    bg=loadImage("background.png")
    title=loadImage("title.png")
    over=loadImage("gameover.png")
    rectwidth=180
    death=loadImage("death.png")
    excit=loadImage("exit.png")
    restart=loadImage("restart.png")
    monsterA=[]
    player=loadImage("player0.png")
    visible=True    
    for j in range(3):
        stage2attack.append(0)
        stage2time.append(millis())
        manymonsterx.append(random(0,500))    
        alive.append(True)
        baldattack.append(loadImage("attack"+str(j)+".png"))
        manymonsterdx.append(random(1,5))
        enemyhealth.append(0)
        hankattack2.append(loadImage("bossattack"+str(j)+".png")) 
    for i in range(0,4,1):
         player7.append(loadImage("player"+str(i)+".png"))# creating a list to store different player location
         monster.append(loadImage("monster"+str(i)+".png"))    
         melee.append(loadImage("wizard"+str(i)+".png"))
         fireballx.append(random(0,width-60))
         firebally.append(0)
         fireball.append(random(10,15))
         ball.append(True)
         hankattack.append(loadImage("boss"+str(i)+".png"))
    for v in range(bullettotalnum): 
        playerbulletx.append(0)
        playerbullety.append(0)
        enemybulletx.append(0)
        enemybullety.append(0)
        playerbulletvisible.append(False)
        enemybulletvisible.append(False)                 
                            
def draw():# drawing different stages
    if stage==0:
         startpage()
    elif stage==1:
         dial1()
    elif stage==2:
         firststage()
    elif stage==3:
         dial2()
    elif stage==4:
         secondstage()
    elif stage==5:
         dial3()
    elif stage==6:
        gameoverpage()
    elif stage==7:
         finaldial()
    elif stage==8:
         bossstage1()
    elif stage==9:
         bossstage2()
    elif stage==10:
         optionaldial1()
    elif stage==11:
         optionaldial2()
    elif stage==12:
         ending1()
    elif stage==13:
         ending2()
    elif stage==14:
         congratspage()
    elif stage==99:
         bonusstage()
    
def dial1():# draw the first dialogue before the game start
    global record1
    image(bg,0,0,width,height)
    image(player,x,y,100,100)
    fill(255)
    rect(0,0,800,400)      
    textSize(30)
    fill(255,0,0)
    if record1==0:
           text("Noctics:",0,25)
           text("Shxt!Where is Choco? Hank is following her.",0,50)
           text("She is now in a grave danger. I have to save her.",0,70)
           text("I have to save her. I won't let him to hurt her",0,90)
           
    elif record1==1:
           text("Secet Lady:",0,25)
           text("If you want to find her.",0,50)
           text("Please go to the Renaissance Hong Kong Harbour View Hotel ",0,70)
           text("And you will find Choco. Run Noctics! Run",0,90)
             
    elif record1==2:
           text("Noctics:",0,25)
           text("I guess I don't have a choice.",0,50)
           text("Wait for me Choco!",0,70)

def dial2():#drawing the second dialogue
    global record2
    image(bg2,0,0,width,height)
    image(player,x,y,100,100)
    fill(255)
    rect(0,0,800,400)
    fill(255,0,0)
    if record2==0:
        text("Noctics:",0,25)
        text("Fuck you Hank! He sets monster to stop me",0,50)
        text("I get hurt. But I cannot stop here",0,70)
        text("I have to save Choco!!!",0,90)
    elif record2==1:
        image(lobby,0,0,width,height)
        image(hank,600,y,100,100)
        image(choco,700,y,100,100)
        text("Hank:",0,25)
        text("Choco, please accept me",0,50)
        text("I don't want to hurt you",0,70)
    elif record2==2:
        image(lobby,0,0,width,height)
        image(hank,600,y,100,100)
        image(choco,700,y,100,100)
        text("Choco:",0,25)
        text("We are friends Hank, why do you do this?",0,50)
        text("Please don't do this",0,70)
    elif record2==3:
        image(lobby,0,0,width,height)
        image(hank,600,y,100,100)
        image(choco,700,y,100,100)
        text("Hank:",0,25)
        text("Sorry, I will",0,50)

def finaldial():
     global record3
     fill(255)
     rect(0,0,800,400)
     image(hank,600,y,100,100)
     image(bg3,0,0,width,height)
     image(player,100,y,100,100)
     if record3==0:
        text("Noctics:",0,25)
        text("Hank, you finally show up!",0,50)
        text("Where is Choco? Your scrum!",0,70)
     elif record3==1:
        text("Hank:",0,25)
        text("Coming to such a place. Quite good!",0,50)
        text("Let's make a deal. If you surrender,",0,70)
        text("I will bring you to Choco.",0,90)
     elif record3==2:
        text("Noctics:",0,25)
        text("What should I do?",0,50)
        text("It may be a trap.",0,70)
        text("Choco....",0,90)
        text("Hint:Your choice will affect the ending and your fate.",0,150)
        text("Please consider what option you should choose.",0,170)
        drawsurrenderbutton("Surrender",450,550)
        drawsurrenderbutton("Fight",650,550) 

def optionaldial1():
    image(bg3,0,0,width,height)
    image(player,100,y,100,100)
    image(hank,600,y,100,100)
    if dial3==0:
        text("Noctics:",0,25)
        text("I won't surrender Hank",0,50)
        text("You hurt Choco",0,70)
        text("You will face the consequences of my anger",0,90)
    elif dial3==1:
        text("Hank:",0,25)
        text("Then now you never find Choco",0,50)
        text("And you will die",0,70)

def optionaldial2():
    image(bg3,0,0,width,height)
    image(player,100,y,100,100)
    image(hank,600,y,100,100)
    if dial4==0:
        text("I choose surrender",0,50)
        text("Noctics:",0,25)
    elif dial4==1:
        text("Hank:",0,25)
        text("Then I will bring you to Choco",0,50)
    elif dial4==2:
        image(lobby,0,0,width,height)
        image(hank,600,y,100,100)
        image(player,100,y,100,100)
        image(choco,700,y,100,100)
        text("Hank:",0,25)
        text("Here is Choco.",0,50)
        text("But I won't let you to get her",0,70)     
        text("You will die in this explosion",0,90)
    elif dial4==3:
        image(lobby,0,0,width,height)
        image(player,100,y,100,100)
        text("Noctics:",0,25)
        text("What you have a plane",0,50)
        text("Shit I have to move fast",0,70)
        text("this place is going to collasped",0,90)
        text("Wait for me Choco I am going to you",0,110)
def drawsurrenderbutton(name,btnx,btny):
        fill(0, 255, 0)
        rect(btnx, btny, 150, 150)
        fill(0)
        textSize(25)    
        text(name, btnx + 10, btny + 30)   
            
def startpage(): #draw start page
    image(bg,0,0,width,height)
    image(title,280,200,200,200)
    fill(255,0,0)
    textSize(50)
    text("Sacrifice",290,400)
    fill(255,255,255,random(135,155))
    textSize(30)
    text("Press any button to start your jouney",100,500)
    text(" Press D or d is move right",100,550)
    text("Press A or a is to move Left",100,600)
    text("Press J or j is to attack",100,650)
    text("Press arrow key and z to control the plane and shoot bullet",50,700)

def firststage():
    global x, monsterdx,monsterx,visible,starttime,b,rectwidth,stage,health
    global score,medkit,restore,sounddelay,sound
    image(bg,0,0,width,height)
    fill(255,0,0)
    rect(70,0,rectwidth,20)
    text("Life:",0,30)
    text("Score:"+str(score),20,50)
    text("Medkit left"+str(medkit),20,70)
    if visible==True and health<11: # these line are for control the player motion
        image(monster2,monsterx,monstery,100,100)
    if stand==True:
        image(player,x,y,100,100)
    if (right):
        x=x+10
        image(player4,x,y,100,100)
    if (attack):
        image(player7[a],x,y,100,100)    
        if ( monsterx-x<=100 and monsterx-x>=0) or (x-monsterx<=100 and x-monsterx>=0) and visible==True:#This is for calculating the hit range of player
             health=health+strength
             punch.play()
             punch.rewind()
             if health<11 or visible==True:#keep adding the score if the monster is not dead yet
                score=score+50
            
    if (left):
        x=x-10
        image(player8,x,y,100,100)
    if x<0:# if the player go out the boundary it will telport them back
        x=0
    if x+100>800:
        x=700
 
    if monsterx>x:
        monsterdx=-3
        
    elif monsterx<x:
        monsterdx=3
    elif monsterx==x:
        monsterdx=0
    monsterx=monsterx+monsterdx
    if(( monsterx-x<=100 and monsterx-x>=0) or (x-monsterx<=100 and x-monsterx>=0) )and health<11 :# if the monster is close to the player it will start attack the player
             image(monster[b],monsterx,monstery,100,100)    
             if (sound<millis()):
                 hurt.play()
                 sound=millis()+sounddelay
             if (starttime<millis()):#It will do the attack move in a sequence of time
                 visible=False  
                 starttime=millis()+delay
                 rectwidth=rectwidth-30
                 b=b+1
                 if b>3:
                     b=2
            
    else :
         visible=True
           
    if rectwidth<0: #if player health go to zero, move to the gameover page
         stage=6           
    elif health>10:# if the monster get defeated, it will move to the next stage
        stage=99
    if rectwidth<60:# if the player health is below a percentage it will play the warning voice
        warning.play()

def ending1():
    image(bg3,0,0,width,height)
    image(player,100,y,100,100)
    image(hank,600,y,100,100)
    if last1==0:
       text("Hank:",0,25)
       text("Your asshole, you kill me.You never find Choco",0,50)
       text("And now I am going to explode the bomb",0,70)
       text("Choco is mine~",0,90)
    elif last1==1:         
         text("Noctics:",0,25)
         text("Shit! Don't do this Hank!",0,50)
    elif last1==2:
         image(bg5,0,0,width,height)
         image(player,100,y,100,100)
         image(chocosleep,600,550,100,100)
         text("Noctics:",0,25)
         text("No it is not True. Tell me it's not True",0,50)
         text("I am very sorry Choco.I should not be impulsed",0,70)
         text("It is all my fault.",0,90)
         text("Please wake up!",0,110)
         text("I am sorry. I am sorry.",0,130)

def ending2():
    image(outside,0,0,width,height)
    image(player,100,y,100,100)
    image(hank,600,y,100,100) 
    image(chocosad,140,y,100,100)
    if last2==0:
        text("Hank:",0,25)
        text("Damn!Why I lose to you",0,50)
    elif last2==1:         
         text("Noctics:",0,25)
         text("This is the power of love.",0,70)
         text("You won't understand it. Hank",0,90)
    elif last2==2:
         text("Hank:",0,25)
         text("Diu, or ng gum sum ar",0,50)
         text("arrrrrrr",0,70)
    elif last2==3:
         text("Noctics:",0,25)
         text("Choco are you ok?",0,70)
         text("I am sorry that I come late",0,90)
         text("Hope I come on time",0,110)
    elif last2==4:
         text("Choco:",0,25)
         text("Lei ho chi ar Noctics",0,50)
         text("I waited  you for so long T.T",0,70)
         text("You are my white horse prince",0,90)
    
         
def congratspage():
    image(good,0,0,width,height)
    image(happy,300,200,150,150)
    text("Congratuation!You pass the game!",200,450)
    text("But is your ending good?",200,500)
    text("Your score is"+str(score),200,550)
    text("Play again or leave the game",200,650)
    image(excit,250,350,70,70)
    image(restart,450,350,70,70)
    
def gameoverpage():
    image(death,0,0,width,height)
    image(excit,250,350,70,70)
    image(restart,450,350,70,70)
    fill(0,0,255)
    textSize(40)
    text("Your Score is:"+str(score),250,250)
    
def secondstage():
    global fireball,firedy,alive,rectwidth,stage,score,manymonsterdx,manymonsterx,x,y     
    global stage2attack,baldattack,wizardlife,wizardexist,starttime,enemyhealth
    global stage2time, magicattack,firebally,meleepic,ball,ballcontrol
    firedy=random(1,10)
    image(bg2,0,0,width,height)
    fill(255,0,0)
    rect(70,0,rectwidth,20)
    text("Life:",0,30)
    text("Medkit left"+str(medkit),20,70)
    text("Score:"+str(score),20,50)
    if (wizardlife<8) and (wizardexist==True):
        image(wizard,wizardx,wizardy,100,100)

    if stand==True:
        image(player,x,y,100,100)
    if (right):
        x=x+10
        image(player4,x,y,100,100)
            
    if (left):
        x=x-10
        image(player8,x,y,100,100)
    if (attack):
         image(player7[a],x,y,100,100)    
         if (wizardx-x<=100 and wizardx-x>=100) or (x-wizardx<=100 and x-wizardx>=0):
            punch.play()
            punch.rewind()
            wizardlife=wizardlife+strength
            if wizardlife<8:
               score=score+100
    if x<0:# if the player go out the boundary it will telport them back
        x=0
    if x+100>800:
        x=700     
    for j in range(3):
         if (alive[j]== True) and (enemyhealth[j]<10):
           image(manymonster, manymonsterx[j],manymonstery,100,100) #drawing a several monster  location
           if manymonsterx[j]> x :
                manymonsterdx[j]=-random(1,5)
           else: 
                manymonsterdx[j]=random(1,5)
           manymonsterx[j]=manymonsterx[j]+manymonsterdx[j]
         if wizardlife>8 and enemyhealth[j]>10:
           stage=7
         if (attack):
           image(player7[a],x,y,100,100)    
           if (manymonsterx[j]-x<=50 and manymonsterx[j]-x>=0) or (x-manymonsterx[j]<=50 and x-manymonsterx[j]>=0) and (alive[j]==True):
                  punch.play()
                  punch.rewind()
                  enemyhealth[j]=enemyhealth[j]+strength
                  if alive[j]==True and enemyhealth[j]<10:
                     score=score+100
         if ((manymonsterx[j]-x<=50 and manymonsterx[j]-x>=0) or (x-manymonsterx[j]-x<=50 and x-manymonsterx[j]>=0)) and (enemyhealth[j]<10):# if one of thwe monster close to player it will start attack
                print enemyhealth[j]
                image(baldattack[stage2attack[j]],manymonsterx[j],manymonstery,100,100)
                hurt.play()
                if (stage2time[j]<millis()):
                    alive[j]=False                 
                    stage2time[j]=millis()+delay
                    rectwidth=rectwidth-5
                    stage2attack[j]=stage2attack[j]+1
                    if stage2attack[j]>2:
                        stage2attack[j]=0
                else:
                        alive[j]=True
    if((wizardx-x<=800 and wizardx-x>=0) or (x-wizardx<=800 and x-wizardx>=0)) and (wizardlife<8): #if wizard is far away to the player, it will use the magic draw different circles shoot to player
                    image(wizardattack,wizardx,wizardy,100,100)
                    for k in range(4):
                        if ball[k]==True:
                            image(fireballimg,fireballx[k],firebally[k],60,60)#drawing different fireball
                            firebally[k]=firebally[k]+fireball[k]
                            if fireballx[k]+60>=x and fireballx[k]<=x+60 and 60+firebally[k]>=y and firebally[k]<=y+100:
                                rectwidth=rectwidth-20
                                hurt.play
                                ball[k]=False
                            if firebally[k]+60>800:
                                firebally[k]=-10
                    if (magicattack<millis()):
                        wizardexist=False              
                        magicattack=millis()+furthertime
                        
        
                    else:
                        wizardexist=True    
    if rectwidth<60:
         warning.play()
    if rectwidth<0:
         stage=6
   
def bossstage1():
    global x, score, hankhealth,rectwidth,hankalive,hankx,monsterdx, hanktime,hankattack,hankattack2
    global hankpunch,stage,hankrush,monsterdx
    image(bg3,0,0,width,height)
    fill(255,0,0)
    rect(70,0,rectwidth,20)
    text("Life:",0,30)
    text("Score:"+str(score),20,50)
    text("Medkit left"+str(medkit),20,70)
    if hankalive==True and hankhealth<30:
        image(hank,hankx,hanky,100,100)
    if stand==True:
        image(player,x,y,100,100)
    if (right):
        x=x+10
        image(player4,x,y,100,100)
    if (attack):
        image(player7[a],x,y,100,100)    
        if ( hankx-x<=100 and hankx-x>=0) or (x-hankx<=100 and x-hankx>=0) and hankalive==True:
             hankhealth=hankhealth+strength
             punch.play()
             punch.rewind()
             if hankhealth<40 or hankalive==True:
                score=score+50
            
    if (left):
        x=x-10
        image(player8,x,y,100,100)
    if x<0:# if the player go out the boundary it will telport them back
        x=0
    if x+100>800:
        x=700
    if x<0:# if the player go out the boundary it will telport them back
        x=0
    if x+100>800:
        x=700
    if rectwidth<60:
        warning.play()
    if rectwidth<0: #if player health go to zero, move to the gameover page
        stage=6   
    elif hankhealth>40:
        stage=12 
    if hankx>x:
        monsterdx=-3    
    elif hankx<x:
        monsterdx=3
    elif hankx==x:
        monsterdx=0
    hankx=hankx+monsterdx
    if(( hankx-x<=50 and hankx-x>=0) or (x-hankx<=50 and x-hankx>=0) )and hankhealth<40:# if the monster is close to the player it will start attack the player
             image(hankattack[hankpunch],hankx,hanky,100,100)
             if (hanktime<millis()):
                 hankalive=False  
                 hanktime=millis()+delay
                 rectwidth=rectwidth-30
                 hankpunch=hankpunch+1
                 if hankpunch>3:
                    hankpunch=0
                    
    elif(( hankx-x<=100 and hankx-x>=50) or (x-hankx<=100 and x-hankx>=50) )and hankhealth<40:# if the monster is close to the player it will start attack the player
             image(hankattack2[hankrush],hankx,hanky,100,100)
             monsterdx=0
             if (hanktime<millis()):
                 hankalive=False  
                 hanktime=millis()+delay
                 rectwidth=rectwidth-30
                 hankrush=hankrush+1# This is for storing different attack motion
                 if hankrush>2:
                     hankrush=0
    else :
         hankalive=True
           
          
def bossstage2():
    global pos,playerplanex,playerplaney,rectwidth,stage
    global playerbulletx,playerbullety,enemybulletx,enemybullety
    global playerbulletvisible,enemyplanex,planespeed,bullettime
    global enemybulletvisible,enemyplanehealth,score
    image(sky,pos,0,width*1.15,height) 
    print enemyplanehealth
    image(sky,pos+width,0,width*1.15,height)
    fill(255,0,0)
    rect(70,0,rectwidth,20)
    text("Life:",0,30)
    text("Score:"+str(score),20,50)
    text("Medkit left"+str(medkit),20,70)
    pos=pos+speed
    image(plane,playerplanex,playerplaney,100,100)
    image(enemyplane,enemyplanex,enemyplaney,100,100)
    enemyplanex=enemyplanex+planespeed
    if enemyplanex+100>800:
        planespeed=-planespeed
    if enemyplanex<0:
        planespeed=-planespeed
           
    if (pos<= -height):
        pos=0
    if (keyPressed):#This is for control the plane
         if key ==CODED:
             if keyCode== UP:
                  playerplaney=playerplaney-5
             if keyCode==DOWN:
                  playerplaney=playerplaney+5
             if keyCode== LEFT:
                  playerplanex=playerplanex-5
             if keyCode==RIGHT:
                  playerplanex=playerplanex+5
    if  playerplaney<0:
          playerplaney=0   
    if playerplaney+100>800:
         playerplaney=700
    if playerplanex<0:
         playerplanex=0
    if playerplanex+100>800:
         playerplanex=700
    for v in range(bullettotalnum):
        if playerbulletvisible[v]==True:
            image(planebullet,playerbulletx[v],playerbullety[v],80,80)
            playerbullety[v]=playerbullety[v]-bulletspeed
        if playerbullety[v]<0:
           playerbulletvisible[v]=False
    if bullettime<millis():
        bullettime=millis()+bulletdelay
        found2=False
        for v in range (bullettotalnum):
# for each bullet
# look for a reusable(not visible) bullet
# if one has not been found
# i.e. found is False and visible is False
            if found2==False and enemybulletvisible[v]==False:
                enemybulletx[v]=enemyplanex # set the bullet’s x y positions
                enemybullety[v]=enemyplaney
                enemybulletvisible[v]=True # make the bullet visible
                found2=True # set found to True to indicate a
# reusable bullet has been found
# so that the loop will not fire another bullet
    for v in range(bullettotalnum):
        if enemybulletvisible[v]==True: # drawing the enemy bullet
           image(enemybullet,enemybulletx[v],enemybullety[v],80,80)
           enemybullety[v]=enemybullety[v]+bulletspeed
        if enemybullety[v]>800:
           enemybulletx[v]=enemyplanex
           enemybullety[v]=enemyplaney
           enemybulletvisible[v]=False
        if (enemybullety[v]+80>=playerplaney) and(enemybullety[v]<playerplaney+100)and (enemybulletx[v]+80>=playerplanex) and (enemybulletx[v]<=playerplanex+100)and enemybulletvisible[v]==True:
           rectwidth=rectwidth-20#If enemy bullet hit player plane player plane health decrease
           enemybulletvisible[v]=False
        if (playerbullety[v]<=enemyplaney) and (playerbulletx[v]+80>=enemyplanex) and ( playerbulletx[v]<=enemyplanex+100) and playerbulletvisible[v]==True:
            enemyplanehealth=enemyplanehealth+1
            playerbulletvisible[v]=False
            score=score+50
    if rectwidth<60:
        warning.play()
    if rectwidth<0: #if player health go to zero, move to the gameover page
        stage=6 
    if enemyplanehealth>30:
        stage=13  
                                                            
                  
def bonusstage():
    global strength
    image(hotel,0,0,width,height)
    text("It's bonus time",100,500)
    text("Win this game and you can get a strength increase",50,550)
    image(rock,100,100,80,80)
    image(scissor,100,200,80,80)
    image(paper,100,300,80,80)
    if robot==1: #Thiis is for drawing different motion of robot choose
         image(hotel,0,0,width,height)
         image(rock,500,100,80,80)
    elif robot==2:
         image(hotel,0,0,width,height)
         image(scissor,500,200,80,80)
    elif robot==3:
         image(hotel,0,0,width, height)
         image(paper,500,100,80,80)     
    if   playeroption==1:
         image(rock,100,100,80,80)      
    elif playeroption==2:
         image(scissor,100,100,80,80)
    elif playeroption==3:
         image(paper,100,100,80,80)
    if (playeroption==1 and robot==1) or (playeroption==2 and robot==2) or (playeroption==3 and robot==3):#These lines are for controling the wining,losing and draw condition
        image(winwin,400,400,100,100)
        text("Pressed any button to go next stage",100,500)
    elif(playeroption==1 and robot==2) or (playeroption==2 and robot==3) or(playeroption==3 and robot==1):
        image(win,400,400,100,100)
        strength=1.5
        text("Pressed any button to go next stage",100,500)
    elif (playeroption==1 and robot==3) or (playeroption==2 and robot==1) or (playeroption==3 and robot==2):
        image(lose,400,400,100,100)    
        text("Pressed any button to go next stage",100,500)
        

def mousePressed():
    global stage, rectwidth,record1, record2,record3,medkit,robot,playeroption
    if stage==6 or stage==14:
       if mouseX>250 and mouseX<250+70  and mouseY>350 and mouseY<350+70:#This is for the ending control for player to choose exit the game and replay the game
            exit()
       elif mouseX>450 and mouseX<450+70 and mouseY>350 and mouseY<350+70:
            setup()
    elif stage==99:
         if (mouseX>100 and mouseX<100+80 and mouseY>100 and mouseY<100+80) or (mouseX>100 and mouseX<100+80 and mouseY>200 and mouseY<200+80) or  (mouseX>100 and mouseX<100+80 and mouseY>300 and mouseY<300+80):        
             robot=int(random(1,4))# if the player choose whether what option. The AI will also choose the option by generating a value
         if (mouseX>100 and mouseX<100+80 and mouseY>100 and mouseY<100+80):
             playeroption=1
         if (mouseX>100 and mouseX<100+80 and mouseY>200 and mouseY<200+80):
             playeroption=2
         if  (mouseX>100 and mouseX<100+80 and mouseY>300 and mouseY<300+80):
             playeroption=3
        
    elif stage==7:
         if mouseX>450 and mouseX<450+100 and mouseY>550 and mouseY<550+100:# this is for the mutliple ending
              stage=11
         elif mouseX>650 and mouseX<650+100 and mouseY>550 and mouseY<550+100:
              stage=10
      
    
def keyPressed():
    global stage,direction,right,left,stand,attack,a ,record1
    global rectwidth,restore,medkit,increase,record2,record3
    global playerplanex,playerbulletx,playerbullety,bulletvisible
    global last2,last1,dial3,dial4
    if key=="D" or key=="d": #if player press different key, the player will perform different motion
        right=True  #jIt make the screen only display the player move right image
        stand=False
    elif key=="j" or key=="J":
        attack=True
        stand=False
        a=a+1
        if a>3:
            a=1
    elif key=="a" or key=="A":
        left=True
        stand=False
    elif key=="k" or key=="K":
        medkit=medkit-1
        rectwidth=rectwidth+increase
        if medkit<0:
             increase=0
             medkit=0
    if stage==0:
         stage=1         
    elif stage==1:
        record1=record1+1
        if record1>2:#This if for if the dial is end it will move to the next stage
            stage=2
    elif stage==3:
          record2=record2+1
          if record2>3:
              stage=4
    elif stage==99:
          if robot>0:
              stage=3
    elif stage==10:
         dial3=dial3+1
         if dial3>1:
             stage=8
    elif stage==11:
         dial4=dial4+1
         if dial4>3:
            stage=9
    elif stage==12:
          last1=last1+1
          if last1>2:
              stage=14       
    elif stage==13:
          last2=last2+1
          if last2>4:
             stage=14
    elif stage==7:
        record3=record3+1
        if record3>2:
            record3=2
    elif stage==9:
        if key=="Z" or key=="z":
           found=False
           for v in range(bullettotalnum):#This is control whether player bullet should be visible
               if found==False and playerbulletvisible[v]==False:
                  playerbulletx[v]=playerplanex
                  playerbullety[v]=playerplaney
                  playerbulletvisible[v]=True
                  found=True
                
                     
def keyReleased():
    global right,stand ,attack ,left
    if key=="d" or key=="D":        #If the player release the key, the player motion will restore to stand motion 
        right=False
        stand=True
    elif key=="j" or key=="J":
        attack=False
        stand=True
    elif key=="a" or key=="A":
        left=False
        stand=True    
        
        
    
    
