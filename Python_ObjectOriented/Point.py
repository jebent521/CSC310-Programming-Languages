from math import cos, sin
class Point:
    count = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        Point.count += 1
    
    def __del__(self):
        Point.count -= 1
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    @classmethod
    def polar(cls, r, theta):
        '''returns the rectangular coordinates for a point at the given polar coordinates'''
        return (cls(r*cos(theta), r*sin(theta)))
    
    @staticmethod
    def centroid(points):
        '''returns centroid of an iterable of  points'''
        x=y=n=0
        for p in points:
            x += p.x
            y += p.y
            n += 1
        return Point(x/n, y/n)