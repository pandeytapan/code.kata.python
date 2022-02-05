from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
width = canvas.width()
height = canvas.height()

segment_length = width / 7 
canvas.drawLine(segment_length, 0, segment_length, height)
canvas.drawLine(2 * segment_length, 0, 2 * segment_length, height)
canvas.drawLine(3 * segment_length, 0, 3 * segment_length, height)
canvas.drawLine(4 * segment_length, 0, 4 * segment_length, height)
canvas.drawLine(5 * segment_length, 0, 5 * segment_length, height)
canvas.drawLine(6 * segment_length, 0, 6 * segment_length, height)

canvas.drawOval(2 * segment_length, height / 4, segment_length, segment_length)
canvas.drawOval(3 * segment_length, height / 4, segment_length, segment_length)
canvas.drawOval(4 * segment_length, height / 4, segment_length, segment_length)

win.wait()
