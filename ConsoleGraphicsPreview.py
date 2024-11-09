import BetterConsoleGraphicsLib as Gl
import math

width = 120
height = 30

movementVar = 0

g = Gl.Grid()
while True:
    # filling grid with chars
    g.fill(width, height, ' ')
    
    # var uses sin to smooth number
    sinfunc = 60 + math.sin(movementVar / 100) * 50
    
    # moveing circle
    g.circle(sinfunc, 15, 4, 4, '0')
    
    # moveing triangle
    # creating dots
    d1 = g.polygon_dot(movementVar, 0, 10, sinfunc, 15)
    d2 = g.polygon_dot(movementVar, 120, 10, sinfunc, 15)
    d3 = g.polygon_dot(movementVar, 240, 10, sinfunc, 15)
    # applying lines to dots for visualization
    g.line(d1, d2, '.')
    g.line(d2, d3, '.')
    g.line(d3, d1, '.')
    # text
    g.text(3, 30, 'Example text from one string and position')
    g.text(2, 30-21, 'Example vertical text', True)
    # square
    g.square(109, 26, 10, 5, 'I')
    # print grid
    g.print()

    # change value of var that makes smooth move
    movementVar += 1