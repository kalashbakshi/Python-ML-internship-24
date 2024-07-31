 # class
class ABC:
    def __init__(self):
        self.a=0
        self.L=[]
        self.C="Sample"
    def abc(self):
        print(self.a)
        print(self.L)
        print(self.C)
 if __name__=="__main__":
     obj=ABC()
     obj.abc()
     print(type(obj))