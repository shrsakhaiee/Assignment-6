class complex :

    def __init__(self, real=None, img=None):
        self.x = real
        self.y = img


    def sum(self, second):
        result=complex()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result

    def multiple(self, second):
        result=complex()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result

    def Submission(self, second):
        result=complex()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result

    def show(self):
        return str(self.x) + str(self.y) 

while True:
    print('addad aval mokhtalet ro vared kon :')
    real1 = int(input('vared kon addad aval mokhtalete => real : '))
    img1 = int(input('vared kon addad aval mokhtalete => img  : '))
    s1 = complex(real1 ,img1)
    print('addad dovom mokhtalet ro vared kon :')
    real2 = int(input('vared kon addad dovom mokhtalete => real : '))
    img2 = int(input('vared kon addad dovom mokhtalete => img  : '))
    s2 = complex(real2, img2)
    while True:
        print('\nmenu:\n1.add\n2.sub\n3.mul\n4.exit')
        c = int(input())
        if c==1:
            print(s1.sum(s2).show())
        if c==2:
            print(s1.Submission(s2).show())
        if c==3:
            print(s1.multiple(s2).show())
        if c==4:
            break