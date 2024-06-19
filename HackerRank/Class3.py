import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
        
    def __add__(self, no):
        new_r = self.r + no.r
        new_i = self.i + no.i
        return Complex(new_r, new_i)
        
    def __sub__(self, no):
        new_r = self.r - no.r
        new_i = self.i - no.i
        return Complex(new_r, new_i)
               
    def __mul__(self, no):
        r1 = self.r 
        r2 = no.r     
        i1 = self.i 
        i2 = no.i
        new_r = r1*r2-i1*i2
        new_i = r1*i2+r2*i1
        return Complex(new_r, new_i)
        
    def __truediv__(self, no):
        r1 = self.r 
        r2 = no.r     
        i1 = self.i 
        i2 = no.i
        num = Complex(r1,i1) * Complex(r2,-1*i2)
        den = r2**2+i2**2
        new_r = num.r/den
        new_i = num.i/den
        return Complex(new_r, new_i)
        
    def mod(self):
        return Complex(math.sqrt(self.r**2 + self.i**2),0)

    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')