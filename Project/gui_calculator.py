#This is the graphical interface for the project

from graphics import *
from calc_functions import * 

class Calculator:
    def__init__(self):
	self.canvas() = self.createGraphics()
	self.display= Display()
	self.display.draw(self.canvas)
	self.keypad= keypad()
	self.keypad.draw(self.canvas)
	self.engine= calculatorEngine()
    def createGraphics(self):
	win = GraphWin("Calculator", 350, 450)
        win.setBackground("purple")
        return win
    def run(self):
	while True:
	    key = self.keypad.getKeyPressed()
	    result = self.engine.addKeyPressed(key)
	    if result == “quit”:
		break
		self.display.setText(result)
    

class CalculatorEngine:
    def__init__(self):
	Self.memory = Memory()
	self.equation= “”
    def addKeyPressed(self, key):
	 rectangle = Rectangle(Point(20,10), Point(250,50)).draw(win)
        color2 = "white"
        rectangle.setFill(color2)
        text = Text(Point(140,25)," ")
        text.draw(win)
        return text
        for i in range(18):
            x,y = get_coords(i)
            if x<mouse.x < x+50 and y< mouse.y < y+50:
                print(get_label(i))
                display.setText(display.getText() + ' ' + get_label(i))
                return get_label(i)
            break
	if key in ['M+', 'M-', 'MR', 'MC']:
	    self.memory.process(key, self.equation)
	    return self.equation
	elif key == '=':
	    return self.solve()

class Keypad:
    def__init__(self):
	self.keypadgraphics = self.createGraphics()
	self.buttons= self.createButtons()
    def createButtons(self):
	coords=[[30,110],[90,110],[150,110],[210,110],
              [30,180],[90,180],[150,180],[210,180],
              [30,250],[90,250],[150,250],[210,250],
              [30,310],[90,310],[150,310],[210,310],
              [150,380],[210,380],[30,380],[270,110],
              [270,180],[270,250],[270,310]]
            return coords[i][0], coords [i][1]
	labels= label = ['7','8','9','/','4','5','6','*','1','2','3',
             '+','+ / -','0','.','-','C','=','M+',
             'M-','MR','MC']
            return label[i]
	color = ['lavender','lavender','lavender','lightblue',
             'lavender','lavender','lavender','lightblue',
             'lavender','lavender','lavender','lightblue',
             'lightblue','lavender','lavender','lightblue',
             'lightblue','lightblue', 'lightblue', 'lightblue'
             'lightblue', 'lightblue']
        size = [50,50,50,50,50,50,50,50,50,
            50,50,50,50,50,50,50,50,50,
            50,50,50,50]
	for i in len(coords):
	    button= Button(coords, label)
	    buttons.append(buttons)
	return buttons
        for i in range(18):
            x,y = get_coords(i)
            button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
            button.setFill(color[i])
            label = Text(Point(x+size[i]/2,y+size[i]/2),get_label(i))
            button.draw(win)
            label.draw(win)
    def getKeyPressed(self):
	p= self.win.getMouse()
	return self.checkKey(p)
    def checkKey(self, p)
	for b in self.buttons:
	    if b.isPressed(p):
	    return.getLabel()
	if len(equation) == 0:
        if label == 'MR':
            equation.append(str(memory))
        elif label not in ['+','-','*','/', '+/-']:
            equation.append(label)
        elif label in ['+','-','*','/']:
            equation.append(" " + label + " ")
        elif label == '+/-':
            equation[-1] = str(-1 * float(equation[-1]))
        elif label == 'MR':
            if equation[-1] in [' + ',' - ',' * ',' / ']:
                equation.append(str(memory))
        else:
            equation[-1] = equation[-1] + label
        return equation

def restart():
    if label == "C":
        result = restart_program()

def equationString(equation):
    equationString=""
    for i in range(len(equation)):
        equationString+=equation[i]
        equationString+=" "
    return equationString

    
def main():
    memory = 0
    result = 0
    win = createCanvas()
    display = createDisplay(win)
    equation = []
    coords = create_buttons(win)
    while True:
        mouse = win.getMouse()
        label = get_input(mouse, display)
        if label == "=":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    display.setText(str(result))
                except:
                    continue
        elif label == "M+":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    memory = memory + result
                    display.setText(str(memory))
                except:
                    continue
        elif label == "M-":
            print(equation)
            if len(equation)>0:
                try:
                    result=getEquation(equationString(equation).split())
                    memory = memory - result
                    display.setText(str(memory))
                except:
                    continue

        elif label == "MC":
            print(equation)
            memory = 0
        
        elif label == "Del":
            if len(equation)==0:
                continue
            else:
                del equation[len(equation)-1]
            print(equation)
            display.setText(equationString(equation))
        elif label == "C":
            equation=[]
            display.setText(equationString(equation))
        elif label == None:
            continue
        else:
            equation = add_equation(equation, label,memory)
            display.setText(equationString(equation))


main()

