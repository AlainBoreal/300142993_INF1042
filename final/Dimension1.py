class point:
    def __init__(self, x=0):
        self.x = x
        
    def dist(self, p1):
        return abs(self.x - p1)
                 
    def midPointD1(p2):
      print(p1.x * p2.x)

    def __repr__(self):
        return f"p({self.x})"

p1 = point(3)
p2 = point(7)

p1.dist
p2.dist

print(f"point1 : {p1}")
print(f"point1 : {p2}")
