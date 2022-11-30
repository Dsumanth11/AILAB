from random import randint
class c:
    def __init__(self,b):
        self.b=b
    def __repr__(self):
        return ("monkey has %d bananas"%self.b)
m=[c(randint(0,50)) for i in range(5)]
print(m)

def no_of_bananas(ma):
    return ma.b

print("max monkey",max(m,key=no_of_bananas))