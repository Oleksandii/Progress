import random







class Hat:
    
    house = ['Griffindor','Slytherin']
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.house)
        print(name,'in',house)


        ...

Hat.sort('Harry')



'''

class Hat:
    def __init__(self):
        self.house = ['Griffindor','Slytherin']

    def sort(self,name):
        house = random.choice(self.house)
        print(name,'in',house)


        ...

hat = Hat()
hat.sort('Harry')
        

'''