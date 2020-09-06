from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()
width = canvas.width()
height = canvas.height()

canvas.setLineWidth(6)
canvas.drawOval(width // 4, height // 4, width // 2, height // 2)
canvas.drawOval(width // 4 + width // 8, height // 4 + height // 8, width // 16, height // 16)
canvas.drawOval(width // 2 + width // 16, height // 4 + height // 8, width // 16, height // 16)
canvas.drawLine(width // 4 + width // 8, height // 2 + height // 8, width // 2  + width // 8, height // 2 + height // 8)

win.wait()
