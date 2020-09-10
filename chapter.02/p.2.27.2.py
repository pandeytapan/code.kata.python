from ezgraphics import GraphicsWindow

window = GraphicsWindow()

canvas = window.canvas()
height = canvas.height()
width = canvas.width()

canvas.setBackground(0, 0, 0)
canvas.setOutline(0xFF, 0x00, 0xFF)

canvas.setFill("Green")
canvas.drawPoly(
    (width/4, 3*height/8), 
    (3*width/4, 3*height/8), 
    (3*width/4, 5*height/8),
    (5*width/8, 5*height/8),
    (5*width/8, 7*height/8),
    (3*width/8, 7*height/8),
    (3*width/8, 5*height/8),
    (width/4, 5*height/8),)

# canvas.drawPoly(
#     (width/4, 3*height/8), 
#     (3*width/4, 3*height/8), 
#     (3*width/4, 5*height/8),
#     (5*width/8, 5*height/8),
#     (5*width/8, 7*height/8),
#     (3*width/8, 7*height/8),
#     (3*width/8, 5*height/8),
#     (width/4, 5*height/8),)

window.wait()
