class Student:
    def __init__(self, name,house ,patronus): # house2=None
        if not name:
            raise ValueError('Missing name')
        
        if house not in ['Griffindor']:
            raise ValueError('Incorrect house')
        self.name = name    
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} {self.house} {self.patronus}'
    
    @classmethod
    def get(cls):
        name = input('Name :')
        house = input('House: ')
        return cls(name,house)
    

def main():
    student = Student.get()

    
if __name__ == '__main__':
    main()











