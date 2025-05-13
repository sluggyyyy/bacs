import dudraw

# Draw a small ladybug (total height 0.08, width approx 0.11)
# at position (x, y)
def draw_ladybug(x, y):
    # Draw ladybug head (small black circle, a bit to right of center
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.filled_circle(x+0.04, y, 0.02)
    # Draw the body
    dudraw.set_pen_color(dudraw.RED)
    dudraw.filled_circle(x, y, 0.04)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.circle(x, y, 0.04)  
    dudraw.line(x-0.04, y, x+0.04, y)
    #  Draw the black spots
    spots = [(-0.02, 0.015), (0.02, 0.015), (-0.02, -0.015), (0.02, -0.015), (0, 0.025), (0, -0.025)]
    for spot in spots:
        dudraw.filled_circle(x+spot[0], y+spot[1], 0.005)
    # Draw the antennae
    dudraw.line(x+0.04, y, x+0.07, y+0.01)
    dudraw.line(x+0.04, y, x+0.07, y-0.01)

def main():
    dudraw.set_canvas_size(400, 400)
    x = 0
    y = 0.25
    
    while True:
        dudraw.clear(dudraw.LIGHT_GRAY)
        draw_ladybug(x, y)
        dudraw.show(50)
        x += 0.01

if __name__ == "__main__":
    main()