#This is the graphical interface for the project

from graphics import *
from calc_functions import * 

def createCanvas():
    win = GraphWin("Calculator",275, 375)
    win.setBackground("purple")
    return win

def get_coords(i):
    coords = [[20,60],[80,60],[140,60],[200,60],[20,120],[80,120],[140,120],[200,120],[20,180],[80,180],[140,180],[200,180],[20,240],[80,240],[140,240],[200,240],[140,300],[200,300]]
    return coords[i][0], coords [i][1]

def get_label(i):
    label = ['7','8','9','/','4','5','6','x','1','2','3','+','+ / -','0','.','-','C','=']
    return label[i]
    
def create_buttons(win):
    color = ['lavender','lavender','lavender','lightblue','lavender','lavender','lavender','lightblue','lavender','lavender','lavender','lightblue','lightblue','lavender','lavender','lightblue','lightblue','lightblue']
    size = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]

    for i in range(18):
        x,y = get_coords(i)
        
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),get_label(i))
        button.draw(win)
        label.draw(win)

def createDisplay(win):
    rectangle = Rectangle(Point(20,10), Point(250,50)).draw(win)
    color2 = "white"
    rectangle.setFill(color2)
    text = Text(Point(140,25),' ')
    text.draw(win)
    return text

def get_input(mouse,display):
    for i in range(18):
        x,y = get_coords(i)
        if x<mouse.x < x+50 and y< mouse.y < y+50:
            print(get_label(i))
            display.setText(display.getText() + ' ' + get_label(i))
            return get_label(i)
            break

def add_equation(equation, label):
    if label in ['+','-','*','/']:
        return equation + " " + label + " "
    else:
        return equation + label

def restart():
    if label == "C":
        result = restart_program()
           
def main():
    win = createCanvas()
    display = createDisplay(win)
    equation = ""
    coords = create_buttons(win)
    while True:
        mouse = win.getMouse()
        label = get_input(mouse, display)
        if label == "=":
            result = get_equation(equation.split())
            display.setText(str(result))
        else:
            equation = add_equation(equation, label)
        

main()


