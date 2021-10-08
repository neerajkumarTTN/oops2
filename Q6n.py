
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self) ->str:
        return f"({self.x},{self.y})"
    def __add__(self,Point2):
        if(isinstance(Point2,Point)):
            a=self.x+Point2.x
            b=self.y+Point2.y
            return(Point(a,b))

        else:
            return "can't add with point"

p1=Point(3,4)
p2=Point(2,6)
p3=p1+p2
print(p3)