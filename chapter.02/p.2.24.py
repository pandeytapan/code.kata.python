from ezgraphics import GraphicsWindow
from ezgraphics import GraphicsCanvas


win = GraphicsWindow()
canvas = win.canvas()

canvas.setFill("pink")
canvas.drawRect(0, 0, canvas.width() // 2, canvas.height() // 2)

canvas.setFill(128, 0 , 128)

canvas.drawRect(canvas.width() // 2, canvas.height() // 2, canvas.width() // 2 - 1, canvas.height() // 2 - 1)
win.wait()
