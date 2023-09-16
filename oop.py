class Point():
    # Function that is automatically called every time we try to create 'Point'
    def __init__(self, x, y):    # All functions acting on object itself are called Methods
        # Allow data to be stored inside the object
        self.x = x
        self.y = y
    
p = Point(2, 8)
print(p.x)
print(p.y)
