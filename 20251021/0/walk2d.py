def walk2d():
    xc, yc = 0, 0
    x, y = 0, 0
    while True:
       xc, yc = yield x, y
       x += xc
       y += yc
