from ezgraphics import GraphicsWindow

window = GraphicsWindow()

canvas = window.canvas()
height = canvas.height()
width = canvas.width()

canvas.setBackground(0, 0, 0)
canvas.setOutline(189,183,107)

# canvas.setFill("Yellow")
# canvas.drawPoly(
#     (width / 2, height / 4), 
#     (width, height / 4), 
#     (width, height / 2),
#     (7 * width / 8, height / 2),
#     (7 * width / 8, 3 * height / 4),
#     (5 * width / 8, 3 * height / 4),
#     (5 * width / 8, height / 2),
#     (width / 2, height / 2),
# )


canvas.setFill(238,232,170)
canvas.drawPoly(
    (width / 4, 3 * height / 8),
    (width / 2, height / 4),
    (width, height / 4),
    (3 * width / 4, 3 * height / 8),
)
canvas.drawPoly(
    (5 * width / 8, 5 * height / 8),
    (7 * width / 8, height / 2),
    (7 * width / 8, 3 * height / 4),
    (5 * width / 8, 7 * height / 8),
)

canvas.drawPoly(
    (3 * width / 4, 3 * height / 8),
    (width , height / 4),
    (width, height / 2),
    (3 * width / 4, 5 * height / 8),
)

canvas.setFill(240,230,140)
canvas.drawPoly(
    (width / 4, 3 * height / 8), 
    (3 * width / 4, 3 * height / 8), 
    (3 * width / 4, 5 * height / 8),
    (5 * width / 8, 5 * height / 8),
    (5 * width / 8, 7 * height / 8),
    (3 * width / 8, 7 * height / 8),
    (3 * width / 8, 5 * height / 8),
    (width / 4,  5 * height / 8),)

window.wait()
