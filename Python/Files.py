

#name = input('What is your name ')

names = []#sorted(names,reverse = false)




with open('Python/names.txt') as file:
    for line in sorted(file):
        print(line.rstrip())


with open('Python/names.txt') as file:
    for line in file:
        print(line.rstrip())
      



'''     

with open('Python/names.txt') as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())



with open('Python/names.txt','a') as file:
    file.write(f'\n{name}')

file = open('Python/names.txt','a')
file.write(f'\n{name}')
file.close()'''