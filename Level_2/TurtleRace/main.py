import time
import random
from turtle import Turtle,Screen

# الشاشة 
window=Screen()
window.title("Turtle Race!")
window.setup(700,700)

# إنشاء السلاحف 
turtles = []
go = (-300,0,300)
colors = ("red", "blue", "green")
for i in range(3):
	turtle=Turtle("turtle")
	turtle.color(colors[i])
	turtle.penup()
	turtle.goto(-340,go[i])
	turtles.append(turtle)

# السلحفاة التي تقوم بالكتابة 
My_turtle = Turtle()
My_turtle.hideturtle()

# فانكشن عرض النتيجة 
def win(is_winner):
	if is_winner:
		window.bgcolor("light blue")
		My_turtle.write("You win!", align="center", font=("arial", 12, "bold"))
	else:
		window.bgcolor("pink")
		My_turtle.write("You lose!", align="center", font=("arial", 12, "bold"))

# فانكشن اللعبة الرئيسية 
def game():
	
	# رسم خط النهاية 
	My_turtle.penup()
	My_turtle.goto(330,-320)
	My_turtle.pendown()
	My_turtle.pensize(10)
	My_turtle.goto(330,320)
	My_turtle.penup()
	My_turtle.goto(0, 0)
	My_turtle.pendown()
	
	# تخمين المستخدم 
	geuss = window.textinput(
	"GEUSS !",
	"Which turtle will win? \nType red, blue, or green :").lower()
	
	# قيمة تستخدم لعمل اللوب 
	race_continue = True
	
	#  السباق ومنطق اللعبة 
	while race_continue:
		for turtle in turtles:
			if turtle.xcor()>310:
				winner_color = turtle.pencolor()
				race_continue = False
			else:
				turtle.forward(random.randint(1,5))
				time.sleep(1/150)
					
	# تحديد الفائز 
	win(winner_color == geuss)

# تشغيل اللعبة 
game()
window.exitonclick()
