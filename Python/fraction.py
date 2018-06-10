class fraction:
        def __init__(self,nu,de):
            self.nu=nu
            self.de=de
            if self.de<0:
                self.nu=self.nu*(-1)
                self.de=self.de*(-1)
        def print_frac():
            print (str(self.nu)+"/"+str(self.de))
