import math
import turtle
import winsound
import random


#Create the screen
wn = turtle.Screen()
wn.tracer(0)
wn.bgcolor('Black')
wn.title('Space Invaders')
wn.bgpic("space_invaders_background.gif")

#Register shapes
wn.register_shape("player.gif")
wn.register_shape("invader.gif")

#Create the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('White')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pensize(4)
border_pen.pendown()
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()


#Set the score to zero
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align='left', font=("Arial", 14, "normal"))
score_pen.hideturtle()


#Create player
player = turtle.Turtle()
player.shape("player.gif")
player.color('Blue')
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

#Player Weapons
weapon1 = turtle.Turtle()
weapon1.speed(0)
weapon1.shape("circle")
weapon1.color('yellow')
weapon1.penup()
weapon1.shapesize(0.5, 0.5)
weapon1.setposition(0, -400)
weapon1.hideturtle()
w1speed = 35
bulletstate = "ready"


#Create an empty enemies list
number_of_enemies = 5
enemies = []
#Create invaders
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    invaderspeed = 0.2
    enemy.penup()
    enemy.color('red')
    enemy.speed(0)
    enemy.setheading(270)
    enemy.shape('invader.gif')
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

#Move the player left and right
def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)
    player.speed = 0
    
left = 0
right = 0
def move_left():
    player.speed = -15
   
   

def move_right():
    player.speed = 15
    
    

def player_weapon():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        weapon1.setposition(player.xcor(), player.ycor() + 10)
        weapon1.showturtle()

#Check if there is a collision between 2 objects
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


#Create keyboard key bindings

wn.listen()
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(player_weapon, 'space')


#Main game loop
fail = 0
while True:
    wn.update()
    
    move_player()
    
    if fail == 1:
        break
    y = weapon1.ycor()
    for enemy in enemies:
        x = enemy.xcor()
        x -= invaderspeed
        enemy.setx(x)
        
        if x < -280 or x > 280:
            for e in enemies: 
                h = e.ycor() - 50
                e.sety(h)
            invaderspeed *= -1

        if y > 280:
            weapon1.setposition(0, -400)
            weapon1.hideturtle()
            bulletstate = 'ready'

        if is_collision(weapon1, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            score += 10
            score_pen.clear()
            scorestring = "Score: {}".format(score)
            score_pen.write(scorestring, False, align='left', font=("Arial", 14, "normal"))
            bulletstate = 'ready'
            weapon1.hideturtle()
            weapon1.setposition(0, -400)
            y = random.randint(150, 250)
            x = random.randint(-200, 200)
            enemy.setposition(x, y)
            
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over!')
            fail = 1
            break

        if enemy.ycor() < -250:
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over!')
            fail = 1
            break
            

    if bulletstate == 'fire':
        y = weapon1.ycor()
        y += w1speed
        weapon1.sety(y)








