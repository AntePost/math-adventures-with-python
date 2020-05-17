#set the range of x­values
xmin = -10
xmax = 10

#range of y­values
ymin = -10
ymax = 10

#calculate the range
range_x = xmax - xmin
range_y = ymax - ymin

def setup():
    global x_scl, y_scl
    x_scl = width / range_x
    y_scl = -height / range_y
    size(600, 600)

def draw():
    global x_scl, y_scl
    background(255)
    translate(width/2, height/2)
    
    grid(x_scl, y_scl)
    
    graphFunction()

def grid(x_scl, y_scl):
    #Draws a grid for graphing
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i*x_scl,ymin*y_scl,i*x_scl,ymax*y_scl)
        line(xmin*x_scl,i*y_scl,xmax*x_scl,i*y_scl)
    for i in range(ymin,ymax+1):
        line(xmin*x_scl,i*y_scl,xmax*x_scl,i*y_scl)
    stroke(0)
    line(0,ymin*y_scl,0,ymax*y_scl)
    line(xmin*x_scl,0,xmax*x_scl,0)

def f(x):
    return 2*x**2 + 7*x - 15

def graphFunction():
    stroke(255,0,0)
    x = xmin
    while x <= xmax:
        fill(0)
        line(x*x_scl,f(x)*y_scl,(x+0.1)*x_scl,f(x+0.1)*y_scl)
        x += 0.1
