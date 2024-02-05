from ezgraphics import GraphicsWindow

# Create the Window and access the canvas
win = GraphicsWindow()
canvas = win.canvas()

# Draw in the canvas
canvas.setFill(255, 0 ,0)
canvas.drawRect(0, canvas.height() // 4 , canvas.width(), canvas.height() // 2 )

canvas.setOutline(255 ,255 ,255)

canvas.drawText(10, canvas.height() // 4 + 10, "Hello World")
win.wait()


