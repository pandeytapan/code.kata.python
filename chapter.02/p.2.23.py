from ezgraphics import GraphicsWindow

# Create the Window and access the canvas
win = GraphicsWindow()
canvas = win.canvas()

# Draw in the canvas
canvas.drawRect(5, 10 ,20, 30)

win.wait()


