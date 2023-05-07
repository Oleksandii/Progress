
#####
i= 1
while i<=3:
    print('Hi')
    i= i+1
######
for i in [0,1,2]:
    print(i)
####
for i in range(0,3): # (3) by default 0
    print(i)
##############
print('meow\t'*3)
##########
while True:
    n= int(input("What's X"))
    if n > 0:
        continue
    elif n<0:
        break
##############
for _ in range(4):
    print('wwww')
#######

def ddd():
    while True:
        i = int(input('Write i'))
        if i>0:
            break
    return i
def kkk():
    res = ddd()
    print(res)
kkk()
#########
def ddd(i):
    while True:
        
        if i>0:
            break
    return i -1
def kkk():
    res = ddd(4)
    print(res)
kkk()


students = ['Ron','Doncic','Space']
for i in range(len(students)):
    print(students[i])

for i in students:
    print(i)

##########
students ={
    'Harry':'Griffindor',
    'Ron':'Griffindor',
    'Drako':'Slytherin'
}
for student in students:
    print(student, students[student])

students1=[
    {'name':'Ron','House':'Griffindor'},
    {'name':'Harry','House':'Griffindor'},
    {'name':'Drako','House':'Griffindor'},
    {'name':'Space','House':None}
]
for student in students1:
    print(student['name'],student['House'])