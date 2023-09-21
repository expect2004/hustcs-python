class Point:
    def __init__(self,x,y,z,h):
        self.x = x
        self.y = y
        self.z = z
        self.h = h
    def getPoint(self):
        return self.x,self.y,self.z,self.h
class Line(Point):
    # 请在下面填入覆盖父类getPoint()方法的代码，并在这个方法中分别得出x - y与z - h结果的绝对值
    ########## Begin ##########
    def getPoint(self):
        x, y, z, h = Point.getPoint(self)
        length_one = x - y if x - y > 0 else y - x
        length_two = z - h if z - h > 0 else h - z
    ########## End ##########
        print(length_one,length_two)
    
