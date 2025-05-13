from __future__ import annotations
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self)->str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: Point)->bool:
        return self.x == other.x and self.y == other.y
    
class Triangle:
    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3

    def __str__(self)->str:
        return f"Vertices: {self.vertex1}, {self.vertex2}, {self.vertex3}"
    
t1 = Triangle(Point(1, 6), Point(5, 3), Point(1, 3))
# t2 = copy.copy(t1)
# t1.vertex1 = Point(8, 9)
# t2.vertex3.x = 63
t3 = copy.deepcopy(t1)