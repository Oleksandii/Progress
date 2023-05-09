import csv



students = []
with open('Python/students.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name': row['name'], 'home':row['home'] })# or row only
)


    #without header
    reader = csv.reader(file)
    for row in reader:# for name,house in reader
        students.append({'name':row[0], 'home':row[1]})# students.append({'name':name, 'home': home})



    '''     
    for line in file:
        name,house = line.strip().split(',')
        student = {'name':name, 'house':house}
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students, key=get_name,reverse = True) : #key = lambda student: student['name']
    print(f"{student['name']} is in {student['house']}")
            
        
        

        name,house = line.split().strip(',')
        #print(f'{name} is in {house}')
        student = {}
        student['name']= name
        student['house']= house
        students.append(student)
for student in students:
    print(f"{student['name']} is in {student['house']}")
    
    
    
###################
    for line in file:
        row = line.split().strip(',')
        print(f'{row[0]} is in {row[1]}')

###########################

#name = input('What is your name ')

names = []#sorted(names,reverse = false)






with open('Python/names.txt') as file:
    for line in sorted(file):
        print(line.rstrip())


with open('Python/names.txt') as file:
    for line in file:
        print(line.rstrip())
      



   

with open('Python/names.txt') as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())



with open('Python/names.txt','a') as file:
    file.write(f'\n{name}')

file = open('Python/names.txt','a')
file.write(f'\n{name}')
file.close()'''