#creation of coordinate data type using oops!!
class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return f"<{self.x_cod},{self.y_cod}>"
    def eucliden_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
    def Distance_From_origin(self):
        return (self.x_cod**2 + self.y_cod**2)**0.5

#checking whether x,y point lie on a given line --> Ax+By+C
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    def Point_on_line(line,Point):
        if line.A*Point.x_cod + line.B*Point.y_cod + line.C == 0:
            return f"({Point.x_cod},{Point.y_cod}) lie on line {line.A}x + {line.B}y + {line.C} = 0"
        else:
            return "Given point does not line on the given line!!"
    def Shortest_distance(self,Point):
        d=(self.A*Point.x_cod + self.B*Point.y_cod + self.C) / (self.A**2 + self.B**2)**0.5
        if d < 0 :
            d = -d
        else:
            pass
        return d
    def Line_intersect(Line,other):
        if Line.A/other.B != Line.B/other.B:
            return "line intersect each other"
        else:
            return " line does not intersect each other"

