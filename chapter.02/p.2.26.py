from ezgraphics import GraphicsWindow

fillname = ('black', 'white')
window = GraphicsWindow()
canvas = window.canvas()

width= canvas.width()
height = canvas.height()
colorWhite = 0
for delta in range (0, width // 2, 40):
    canvas.setFill(fillname[colorWhite])
    canvas.drawOval(delta , delta, width - 2 * delta, height - 2 * delta)
    colorWhite = not colorWhite

window.wait()
