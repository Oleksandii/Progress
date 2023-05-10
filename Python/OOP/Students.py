
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
    
    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter
    def house(self, house):
        if house not in ['Griffindor']:
            raise ValueError('Incorrect house')
        self._house = house
        
    
    def  magic(self):
        match self.patronus:
            case 'Snake':
                return 'SSSHHHHH'
            case 'Stag':
                return 'Igogo'
            case _:
                return 'Do not have'




def get_student():
    name = input('Name : ')
    house = input('House : ')
    patronus = input('Patronus :')
    student = Student(name,house, patronus)
    return student
    '''student = Student()
    student.name= 'Oleksii'
    student.house = 'Griffindor'
    student.patronus = input('What is your patronus')
    return student '''# or name = '' houes = '' student = Student(name,house)

def main():

    student = get_student()
    student.house = 'hi'
    print(student)
main()







'''


############################
class Student:
    ...
def get_student():
    student= Student()
    student.name= 'Oleksii'
    return student

def main():

    student = get_student()
    print(student.name)
main()








'''