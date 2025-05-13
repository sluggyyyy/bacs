"""
    Description of program: Simulates particle physics in multiple forms!
    Filename: morgan_project6_particles.py
    Author: Zachary Morgan  
    Date: 03/07/2025
    Course: COMP1352
    Assignment: Project 6 - Particle System
    Collaborators: Devin Schiffli
    Internet Source: geeksforgeeks, dudraw documentation, videos on Canvas
"""

import math
import dudraw
from dudraw import Color
from random import randint, uniform

class Vector:
    def __init__(self, some_x=0, some_y=0):
        self.x = some_x
        self.y = some_y

    def limit(self, l):
        if(self.length() >= l):
            self.resize(l)
        # Added a return to this method so that I can use it in Marbles class
        return self

    def resize(self, l):
        length = math.sqrt(self.x ** 2 + self.y**2)
        self.x *= (l/length)
        self.y *= (l/length)

    def __add__(self, other_vector):
        return Vector(self.x+other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        return Vector(self.x-other_vector.x, self.y - other_vector.y)

    def __isub__(self, other_vector):
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def divide(self, s):
        self.x /= s
        self.y /= s

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_in_radians(self):
        return math.tan((self.y/self.x))

class Particle:
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        self.pos = Vector(x_pos, y_pos)
        self.vel = Vector(x_vel, y_vel)
        self.size = size
        self.lifetime = lifetime
        self.color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.lifetime = lifetime
        
    def has_expired(self):
        if self.lifetime <= 0:
            return True
        else: 
            return False
    
    def move(self):
        if not self.has_expired():
            self.pos += self.vel
            self.lifetime -= 1
            
"""
Class that defines how particles should be initialized, if they have 'expired' (lifetime is decremented by move() method),
and defines movement by adding velocity to it's current position
"""

class AcceleratingParticle(Particle):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        super().__init__(x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.acc = Vector(x_acc, y_acc)
        
    def move(self):
        self.vel += self.acc
        super().move()

"""
Subclass of Particle class
Defines particles that are accelerating, inherits from Particle class and adds an acceleration vector,
Defines accelerating particle's movement by adding acceleration factor to object's velocity
"""

class SparkParticle(Particle):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        super().__init__(x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.color = dudraw.ORANGE
        
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.line(self.pos.x, self.pos.y, self.pos.x + self.vel.x, self.pos.y + self.vel.y)
        
"""
Subclass of Particle, initializes class with parent class's init method with the only new variable being color

draw() method sets pen color to self.color (ORANGE) and draws lines of length (position) to (position + velocity)
"""
        
class FireParticle(Particle):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, size, lifetime):
        super().__init__(x_pos, y_pos, x_vel, y_vel, size, lifetime)
        self.red = 255
        self.green = 255
        
    def draw(self):
        if self.green > 0:
            self.green -= 5
        dudraw.set_pen_color_rgb(self.red, self.green, 0)
        dudraw.filled_circle(self.pos.x, self.pos.y, 0.02)
        
    def move(self):
        super().move()
        self.size -= 1
        
"""
Subclass of Particle class, uses parent's __init__ method and sets red variable to 255 and green variable to 255
(to be decremented later)

draw() method decrements green value by 5 to approach fully red color, draws filled circles at x position and y position of size 0.02
move() method follows suit of parent class's but also decrements size by 1
"""

class FireworkParticle(AcceleratingParticle):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        super().__init__(x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime)
        self.color = Color(randint(0,255), randint(0,255), randint(0,255))
    
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_square(self.pos.x, self.pos.y, self.size)
        
"""
Subclass of AcceleratingParticle class, inherits from parent's init method but sets a random color
draw() method draws random colored squares 
"""

class MarbleParticle(AcceleratingParticle):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime):
        super().__init__(x_pos, y_pos, x_vel, y_vel, x_acc, y_acc, size, lifetime)
        self.color = Color(randint(0,255), randint(0,255), randint(0,255))

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.pos.x, self.pos.y, self.size)

"""
Sublass of AcceleratingParticle, uses parent class's init method but sets a random color
draw() method draws random colored circles
"""

class ParticleContainer:
    def __init__(self, x_pos, y_pos):
        self.particles = []
        self.pos = Vector(x_pos, y_pos)
    
    def animate(self):
        for particle in self.particles:
            particle.move()
            particle.draw()
        self.particles = [particle for particle in self.particles if not particle.has_expired()]

"""
Initializes by setting an empty list of particles, and a position vector
animate() method calls each particle's move and draw method, expired particles are removed from the list
"""

class Firework(ParticleContainer):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)    
        self.acc = Vector(0, uniform(-0.008, -0.012))
        self.size = 0.004
        self.lifetime = 50
        for i in range(500):
            self.velocity = Vector(uniform(-0.04, 0.04), uniform(-0.04, 0.04))
            self.particles.append(FireworkParticle(self.pos.x, self.pos.y, self.velocity.x, self.velocity.y, self.acc.x, self.acc.y, self.size, self.lifetime))

"""
Subclass of ParticleContainer
Calls ParticleContainer class's init function
Sets an acceleration vector
Sets a size for each individual particle
Sets lifetime to 50
For 500 particles, set velocity to be randomized between certain values
Append particles to the list created by ParticleContainer class
"""

class Marbles(ParticleContainer):
    def __init__(self):
        # Calls super() init function initializing with random x,y positions
        super().__init__(uniform(0.05, 0.95), uniform(0.05, 0.95))
        # Sets up acceleration vector
        self.acc = Vector(0, uniform(-0.001, -0.002))
        self.size = 0.05
        self.lifetime = 500
        # Creates 10 marbles with randomized velocities
        for i in range(10):
            self.velocity = Vector(uniform(-0.04, 0.04), uniform(-0.04, 0.04))
            self.particles.append(MarbleParticle(self.pos.x, self.pos.y, self.velocity.x, self.velocity.y, self.acc.x, self.acc.y, self.size, self.lifetime))
    
    # Initialize method for handling physics
    def animate(self):
        # Call ParticleContainer's animate method
        super().animate()
        
        # Loop over marbles in particles list...
        # If any particles are out of bounds, move them by magnitude marble.size
        # Set velocity to reverse direction
        for marble in self.particles:
            if marble.pos.x - marble.size <= 0 and marble.vel.x < 0:
                marble.pos.x = marble.size
                marble.vel.x *= -1 

            if marble.pos.x + marble.size >= 1 and marble.vel.x > 0:
                marble.pos.x = 1 - marble.size
                marble.vel.x *= -1      

            if marble.pos.y - marble.size <= 0 and marble.vel.y < 0:
                marble.pos.y = marble.size
                marble.vel.y *= -1  

            if marble.pos.y + marble.size >= 1 and marble.vel.y > 0:
                marble.pos.y = 1 - marble.size
                marble.vel.y *= -1  
            
            # Dampen the marble's velocities so they aren't so fast
            marble.vel.limit(marble.vel.length() * 0.95)
        
        # Loop over particles list...
        for i in range(len(self.particles)):
            # Nested loop looping over self.particles AGAIN, 
            # incrementing by i + 1 (so that we aren't checking duplicate marbles)
            for j in range(i + 1, len(self.particles)):
                # Set up marble variables
                marble1 = self.particles[i]
                marble2 = self.particles[j]
                
                # Calculate distance between marbles x positions to be used in a distance vector
                distancex = math.sqrt((marble1.pos.x - marble2.pos.x) ** 2)
                # Calculate distance between marbles y positions to be used in a distance vector
                distancey = math.sqrt((marble2.pos.y - marble1.pos.y) ** 2)
                # Calculate distance between marbles outside of vector
                distance = math.sqrt(distancex**2 + distancey**2)
                # Create distance vector with individual distance values
                distance_vector = Vector(distance, distancey)

                # If the marbles are touching...
                if distance <= marble1.size + marble2.size:
                    # Increment the velocity by magnitude of distance vector, but limit speed to 0.02 as stated in the video
                    marble1.vel += distance_vector.limit(0.02)
                    # Repeat for second marble but decrement instead
                    marble2.vel -= distance_vector.limit(0.02)
                    
"""
Subclass of ParticleContainer
Marble class with physics (annotated inside of class)
"""
    
class Emitter(ParticleContainer):
    def __init__(self, x_pos, y_pos, fire_rate):
        super().__init__(x_pos, y_pos)
        self.fire_rate = fire_rate

"""
Subclass of ParticleContainer, uses its init method
Sets fire_rate variable that will later be used to control how many particles are being generated per frame
"""

class Fire(Emitter):
    def __init__(self, x_pos, y_pos, fire_rate):
        super().__init__(x_pos, y_pos, fire_rate)
        self.size = uniform(0.01, 0.03)
        self.lifetime = 50
    def animate(self):
        for i in range(self.fire_rate):
            self.velocity = Vector(uniform(-0.002, 0.002), uniform(0.002, 0.005))
            self.particles.append(FireParticle(self.pos.x, self.pos.y, self.velocity.x, self.velocity.y, self.size, self.lifetime))
        super().animate()

"""
Subclass of Emitter, calls its init function, and sets size to a random number and lifetime to 50
Uses a loop to create fire particles in range of fire_rate variable
Sets velocity Vector to random x,y values
Append particles to particles list in ParticleContainer class
Call ParticleContainer's animate method
"""
        
class Sparkler(Emitter):
    def __init__(self, x_pos, y_pos, fire_rate):
        super().__init__(x_pos, y_pos, fire_rate)
        self.size = 0.04
        self.lifetime = 3
    def animate(self):
        dudraw.set_pen_color(dudraw.WHITE)
        dudraw.line(self.pos.x, self.pos.y, self.pos.x, self.pos.y - 0.5)
        for i in range(self.fire_rate):
            self.velocity = Vector(uniform(-0.07, 0.07), uniform(-0.07, 0.07))
            self.particles.append(SparkParticle(self.pos.x, self.pos.y, self.velocity.x, self.velocity.y, self.size, self.lifetime))
        super().animate()
        
"""
Subclass of Emitter, calls its init function, and sets size to a random number and lifetime to 3
animate() method draws the sparkler stick, loops length of fire rate, inside of loop sets up velocity vector to random values
Appends particles to particles list in ParticleContainer class
Calls ParticleContainer's animate method
"""
        
def main():
    # Set Canvas Size
    dudraw.set_canvas_size(400, 400)
    # Initialize empty list of containers
    containers = []
    # Sets up animation loop
    while True:
        # Clear canvas with black color
        dudraw.clear(dudraw.BLACK)
        
        # Loops over containers list and animates each container using ParticleContainer's animate class
        for container in containers:
            container.animate()
        
        # Returns true if the user has typed a key since the last loop iteration
        if dudraw.has_next_key_typed():
            # If they have, set key variable to the key that was typed
            key = dudraw.next_key_typed()
            # If the key was 'f', append a Firework object to list of containers (will be animated upon next loop iteration)
            if key == 'f':
                mouse_x = dudraw.mouse_x()
                mouse_y = dudraw.mouse_y()
                containers.append(Firework(mouse_x, mouse_y))
        # If the mouse was clicked, append a Marble object to list of containers (will be animated upon next loop iteration)
        if dudraw.mouse_clicked():
            containers.append(Marbles())
        
        # Permanently append a Fire object that is animated upon each iteration
        containers.append(Fire(0.25, 0.25, 1))
        # Permanently append a Sparkler object that is animated upon each iteration
        containers.append(Sparkler(0.75, 0.75, 1))
        # Update frame every 40ms
        dudraw.show(40)
        
    

if __name__ == "__main__":
    main()