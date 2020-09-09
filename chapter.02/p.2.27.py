from ezgraphics import GraphicsWindow

window = GraphicsWindow()

canvas = window.canvas()

canvas.setBackground(0, 0, 0)
canvas.setOutline(0xFF, 0x00, 0xFF)
canvas.drawRectangle(10, 10, 50, 50)
window.wait()
