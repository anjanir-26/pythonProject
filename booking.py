class two:
    def retc(self,l,b):
        print("perimeter of rectangle is",2*(l+b))
        print("area of rectangle is",l*b)
    def triangle(self,a,b,c):
        print("perimeter of triangle is",a+b+c)
        print("area of triangle is",0.5*b*c)
    def square(self,a):
        print("perimeter of square is",4*a)
        print('area of square is ',a*a)
a=two();
a.retc(2,3)
a.triangle(1,3,2)
a.square(4)