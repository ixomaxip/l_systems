#Turtle graphics of L-systems

from math import pi
import turtle as tr

def getWord(axiom='F', newf='F', newb='b', newx='X', newy='Y', level=1):
    #input word for turtle
    W = axiom
    
    while level > 0:
        T = ''
        for c in W:
            #if (c=='[') or (c==']') or (c=='+') or (c=='-'): T += c
            if c == 'F': T += newf
            elif c == 'b': T += newb
            elif c == 'X': T += newx
            elif c == 'Y': T += newy
            else: T += c
        W = T
        level -= 1
    print('Path in steps: ', calcPath(W))
    return W
    
def getTempl(name='default', level=1):
    #Pre-defined generators
    
    #Dictionary
    d = {}
    d['default'] = ('F', 'F', 'b', 'X', 'Y', pi/3, 0)
    d["Bush"] = ('F', '-F+F+[+F-F-]-[-F+F+F]', 'b', 'X', 'Y', pi/8, 0)
    d["GilbertCrv"] = ('X', 'F', 'b', '-YF+XFX+FY-', '+YF-YFY-FX+', pi/2, 0)
    d["GosperCrv"] = ('XF', 'F', 'b', 'X+YF++YF-FX--FXFX-YF+', '-FX+YFYF++YF+FX--FX-Y', pi/3, 0)
    d["Serpinski"] = ('FXF--FF--FF', 'FF', 'b', '--FXF++FXF++FXF--', 'Y', pi/3, 0)
    
    #Getting parameters
    a, f, b, x, y, theta, alpha = d[name]
    #Generating word
    w = getWord(axiom=a, newf=f, newb=b, newx=x, newy=y, level=level)
    return (w, theta, alpha)

def calcPath(word):
    #Calculate a number of steps
    w = word.replace('+','').replace('[','').replace(']','').replace('-','').replace('X','').replace('Y','').replace('v','')

    return len(w)
    
def tGraph(word='F', theta=0, alpha=0, step = 10, x0=0, y0=0):
    #Run, turtle, RUN!!!
    #tr.clear()
    tr.radians()
    tr.speed(0)

    tr.pu()
    tr.setx(x0)
    tr.sety(y0)
    tr.seth(alpha)
    tr.pd()

    st = []
    for c in word:
        if c == 'F':
            tr.fd(step)
        if c == 'b':
            tr.pu()
            tr.bk(step)
            tr.pd()
        if c == '[':
            st.append({'x': tr.xcor(), 'y': tr.ycor(), 'ang': tr.heading()})
        if c == ']':
            pos = st.pop()
            tr.pu()
            tr.setx(pos['x'])
            tr.sety(pos['y'])
            tr.seth(pos['ang'])
            tr.pd()
        if c == '+':
            tr.lt(theta)
        if c == '-':
            tr.rt(theta)


wS, thS, aS = getTempl(name="Serpinski", level=4)
tGraph(wS, thS, aS)
