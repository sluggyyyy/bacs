### PART 1 ###

# import dudraw
# def draw_circles(x: float, y: float, r: float, n: int):
#     if n == 0:
#         return
#     else:
#         draw_circles(x + r, y, r/2, n - 1)
#         dudraw.circle(x, y, r)
#         draw_circles(x - r, y, r/2, n - 1)
#         dudraw.circle(x, y, r)

# dudraw.set_pen_color(dudraw.BLACK)
# draw_circles(0.5, 0.5, 0.25, 6)
# dudraw.show(10000)

### PART 2 ###

from math import cos, sin, radians
import dudraw

def end_point(start_x:float, start_y:float, length:float, angle:float):
    end_x = start_x + length * cos(radians(angle))
    end_y = start_y + length * sin(radians(angle))
    return (end_x, end_y)

def draw_recursive_tree(x: float, y: float, length:float, angle: float, n: int):
    if n == 0:
        return
    else:
        end = end_point(x, y, length, angle)
        dudraw.line(x, y, end[0], end[1])
        draw_recursive_tree(end[0], end[1], length * 0.7, angle + 45, n - 1)
        draw_recursive_tree(end[0], end[1], length * 0.7, angle - 45, n - 1)

draw_recursive_tree(0.5, 0, 0.25, 90, 6)
dudraw.show(10000)
