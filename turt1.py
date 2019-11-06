import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.width(3)
	t.down()
	t.seth(h)
	for i in range (1,10):
			t.pencolor("black")
			t.forward(l)
			t.rt(tn)
			
def circle(t):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (0,10):
		t.forward(10)
		t.rt(36)
		
def circlefill(t,x,y,l):
	print("circle")
	t.penup()
	t.goto(x,y+r)
	t.down()
	t.begin_fill()
	t.color("#000000") 
	for i in range (1,40):
		tn = 9
		if (i > 10 and i <20):
			tn = 5
		t.forward(l)
		t.rt(tn)
	t.end_fill()
		
def matrix():
	print("matrix")

def square(t,x,y):
	t.goto(x,y)
	t.penup()
	t.begin_fill()
	tcolor = "#0000ff"
	t.color(tcolor)
	t.forward(100)
	t.rt(90)
	t.forward(90)
	t.rt(90)
	t.forward(80)
	t.rt(90)
	t.forward(70)
	t.end_fill()

def main():
    x = -400; y = 0
    w = turtle.Screen()
    w.setup(1500, 1000)
    w.clear()
    w.bgcolor("#ffffff")
    t = turtle.Turtle()
    t.speed(0)
    t.penup
    t.goto(0,0)
    t.begin_fill()
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,11,90)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,50,45,180)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,11,0)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,45,90)
    t.goto(260,-150)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,45,90)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,11,270)
    
    t.goto(145,-270)
    t.goto(140,-300)
    t.goto(135,-270)
    
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,11,180)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,45,270)
    t.goto(0,0)
    tcolor = "#00ff00";t.color(tcolor)
    arcR(t,x,y,25,45,270)
    t.end_fill()
    
    t.penup()
    t.right(130)
    t.forward(250)
    t.right(90)
    t.forward(100)
    t.color("red")
    t.pendown()
    t.begin_fill()
    t.forward(10)
    t.circle(10)
    t.end_fill()
    
    t.penup()
    t.forward(30)
    t.color("red")
    t.pendown()
    t.begin_fill()
    t.forward(10)
    t.circle(10)
    t.end_fill()
    
    '''t.speed(0)
    t.color("#000000")
    t.forward(50)
    square(t,x,y)
    circle(t)
	'''
    w.exitonclick()
if __name__ == '__main__':
	main()
	
'''
#apt install python3-tk
	


wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
