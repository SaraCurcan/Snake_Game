import turtle
import random


snake=turtle.Turtle()
snake.color('yellow')
snake.shape('triangle')
snake.shapesize(1.5)
snake.up()
s=turtle.Screen()

food=turtle.Turtle()
food.hideturtle()
food.up()
food.shape('circle')
food.color('red')
food.shapesize(1)
food_pos=None

turtle.setundobuffer(2)

snake_body=[]

score=0
score_display=turtle.Turtle()
score_display
score_display.width(5)

def background():
    s.bgcolor('beige')
    s.setup(width=400,height=400)

def draw_margins():
    t=turtle.Turtle()
    t.hideturtle()
    t.up()
    t.speed('fastest')
    t.goto(-150,-150)
    t.down()
    t.width(3)
    t.fillcolor('darkgreen')
    t.begin_fill()
    for i in range(4):
        t.forward(300)
        t.left(90)
    t.end_fill()

def turn_left():
    if snake.heading()!=0:
        snake.setheading(180)
def turn_right():
    if snake.heading()!=180:
        snake.setheading(0)
def go_up():
    if snake.heading()!=270:
        snake.setheading(90)
def go_down():
    if snake.heading()!=90:
        snake.setheading(270)

def move_forward():
    global snake_body
    if check_game_over():
        show_game_over()
        return
    for i in range(len(snake_body)-1,0,-1):
        x=snake_body[i-1].xcor()
        y=snake_body[i-1].ycor()
        snake_body[i].goto(x,y)

    if len(snake_body)>0:
        snake_body[0].goto(snake.xcor(),snake.ycor())

    check_distance_from_food()
    snake.forward(10)
    show_score()
    s.ontimer(move_forward, 50)

def generate_food():
    global food_pos
    x=random.randint(-138,138)
    y=random.randint(-138,138)
    food.setposition(x,y)
    food.showturtle()
    food_pos=(x,y)


def check_game_over():
    if snake.xcor()>137 or snake.xcor()<-137 or snake.ycor()>137 or snake.ycor()<-137:
        return True
    for clone in snake_body[:-1]:
        if snake.distance(clone)<9:
            return True
    return False

def check_distance_from_food():
    global food_pos
    global score
    if snake.distance(food_pos)<15:
        score+=1
        increase_length()
        generate_food()

    
def increase_length():
    global snake_body
    body_segment=turtle.Turtle()
    body_segment.hideturtle()
    body_segment.speed(0)
    body_segment.color('yellow')
    body_segment.shape('square')
    body_segment.shapesize(1)
    body_segment.up()
    if len(snake_body)>0:
        body_segment.setposition(snake_body[len(snake_body) - 1].xcor(), snake_body[len(snake_body) - 1].ycor())
    else:
        body_segment.setposition(snake.xcor(),snake.ycor())
    body_segment.showturtle()
    snake_body.append(body_segment)

def show_game_over():
    message=turtle.Turtle()
    message.up()
    message.hideturtle()
    message.setposition(0,125)
    message.width(5)
    message.color('red')
    message.write('GAME OVER',align='center',font=15)

def show_score():
    score_display.clear()
    score_display.up()
    score_display.hideturtle()
    score_display.setposition(-125, 125)
    score_display.write(f"Score : {score}")

def start_game():
    snake.showturtle()
    background()
    draw_margins()
    generate_food()
    move_forward()


s.listen()
s.onkey(go_up,'Up')
s.onkey(go_down,'Down')
s.onkey(turn_left,'Left')
s.onkey(turn_right,'Right')

start_game()

s.mainloop()