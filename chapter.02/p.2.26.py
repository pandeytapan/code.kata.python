from ezgraphics import GraphicsWindow

window = GraphicsWindow()
canvas = window.canvas()

width= canvas.width()
height = canvas.height()

for delta in range (0, width // 2, 40):
    canvas.drawOval(delta , delta, width - 2 * delta, height - 2 * delta)

window.wait()
