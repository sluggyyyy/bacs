import dudraw
def sierpinski(l: float, b: float, r: float, t: float): 
    if (t-b) < 0.01:
        dudraw.set_pen_color_rgb(int(255*l), int(225*b), 255-int(255*b))
        dudraw.filled_triangle(l, b, r, b, l, t)
    else:
        sierpinski(l, b, (l+r)/2, (t+b)/2)
        sierpinski((l+r)/2, b, r, (t+b)/2)
        sierpinski(l, (b+t)/2, (l+r)/2, t)

dudraw.set_canvas_size(400, 400)
sierpinski(0,0,1,1)
dudraw.show(10000)