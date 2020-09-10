from ezgraphics import GraphicsWindow

window = GraphicsWindow()

canvas = window.canvas()
height = canvas.height()
width = canvas.width()

canvas.setBackground(0, 0, 0)
canvas.setOutline(0xFF, 0x00, 0xFF)
canvas.drawRectangle(width / 4, height / 4, width / 2, height / 2)
canvas.drawLine(width / 4, height / 4, width / 2, 0)
canvas.drawLine(width / 2, 0, 3 * width / 4, height / 4)
canvas.drawRectangle(3 * width / 8, height / 2, width / 4, width / 4)
window.wait()
