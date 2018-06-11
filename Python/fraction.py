import math
class fraction:
        def __init__(self,nu,de):
            self.nu=int(nu)
            self.de=int(de)
            if self.de == 0:
                raise Exception('denominator is Zero')
            if self.de<0:
                self.nu=self.nu*(-1)
                self.de=self.de*(-1)
            gcd=math.gcd(abs(self.nu),abs(self.de))
            if gcd!=0:
                self.nu=self.nu/gcd
                self.de=self.de/gcd

        def print_frac(self):
            print (str(int(self.nu))+"/"+str(int(self.de)))

        def add(self,frac0):
            return fraction(self.nu*frac0.de+self.de*frac0.nu,self.de*frac0.de)

        def sub(self,frac0):
            return fraction(self.nu*frac0.de-self.de*frac0.nu,self.de*frac0.de)

        def mul(self,frac0):
            return fraction(self.nu*frac0.nu,self.de*frac0.de)

        def div(self,frac0):
            return fraction(self.nu*frac0.de,self.de*frac0.nu)
