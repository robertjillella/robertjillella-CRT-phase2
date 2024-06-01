class student:
    def __init__(self,name,mm,em,pm):
        self.hi=name
        self.maths=mm
        self.english=em
        self.physics=pm
    
    def details(self):
        print('name',self.hi)
        print('maths',self.maths)
        print('eng',self.english)
        print('phy',self.physics)

me=student('narasimha',100,10,1.1)
me2=student('harish',101,221,43)
me3=student('lokesh',114,25,11)


me.details()
me2.details()
me3.details()