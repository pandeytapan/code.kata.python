from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()

canvas.drawOval(canvas.width() // 4, canvas.height() // 4, canvas.width() // 2, canvas.height() // 2)
canvas.drawOval(canvas.width() // 4 + canvas.width() // 8, canvas.height() // 4 + canvas.height() // 8, canvas.width() // 16, canvas.height() // 16)
canvas.drawOval(canvas.width() // 2 + canvas.width() // 16, canvas.height() // 4 + canvas.height() // 8, canvas.width() // 16, canvas.height() // 16)
canvas.drawLine(canvas.width() // 4 + canvas.width() // 8, canvas.height() // 2 + canvas.height() // 8, canvas.width() // 2  + canvas.width() // 8, canvas.height() // 2 + canvas.height() // 8)

win.wait()
