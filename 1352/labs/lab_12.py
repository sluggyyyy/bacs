import random
from dudraw import Color
import dudraw

####### Bouncing Shape ###############
class BouncingShape:
    def __init__(self, x :float, y:float, xv:float, yv:float, s:float):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = xv
        self.y_vel = yv
        self.size = s
        self.color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    

    def move(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel 
        if ((self.x_pos + self.size > 1 and self.x_vel > 0) or 
            (self.x_pos - self.size < 0 and self.x_vel < 0)):
            self.x_vel *= -1

        if ((self.y_pos + self.size> 1 and self.y_vel > 0) or
            (self.y_pos -self.size < 0 and self.y_vel < 0)):
            self.y_vel *= -1  

    def draw(self):
        #We don't know how to draw a generic shape so leave this as is
        pass

class BouncingCircle(BouncingShape):
    def __init__(self, x :float, y:float, xv:float, yv:float, radius:float):
        super().__init__(x, y, xv, yv, radius)
        self.color = Color(0, 0, 255)
        self.radius = radius
    
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_pos, self.y_pos, self.radius)
        
class WobblyCircle(BouncingCircle):
    def __init__(self, x :float, y:float, xv:float, yv:float, s:float):
        super().__init__(x,y,xv,yv,s)
        self.color = Color(255, 0, 0)
        
    def move(self):
        dudraw.set_pen_color(self.color)
        super().move()
        self.x_pos += random.uniform(-0.02, 0.02)
        self.y_pos += random.uniform(-0.02, 0.02)
        
class PatrollingSquare(BouncingShape):
    def __init__(self, x :float, y:float, xv:float, yv:float, s:float):
        # call the parent constructor
        super().__init__(x, y, xv, yv, s)
        # set the color to green
        self.color = Color(0, 255, 0)
        # add step_count and set it to 0
        self.step_count = 0

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_square(self.x_pos, self.y_pos, self.size)

    def move(self):
        super().move()
        self.step_count += 1
        if self.step_count == 30:
            self.x_vel = random.uniform(-0.05,0.05)
            self.y_vel = random.uniform(-0.05,0.05)
            self.step_count = 0
    
def main():
    dudraw.set_canvas_size(600, 600)
    shapes = [BouncingCircle(random.random(), random.random(), random.uniform(-0.02, 0.02), random.uniform(-0.02, 0.02), 0.05), WobblyCircle(random.random(), random.random(), random.uniform(-0.02, 0.02), random.uniform(-0.02, 0.02), 0.05), PatrollingSquare(random.random(), random.random(), random.uniform(-0.04, 0.04), random.uniform(-0.04, 0.04), 0.04)]
    
    while True:
        dudraw.clear(dudraw.WHITE)
        for shape in shapes:
            shape.move()
            shape.draw()
        dudraw.show(50)
        
if __name__ == '__main__':
    main()