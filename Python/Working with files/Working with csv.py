import csv
name = 'hARRY1'
house = 'Griffindor1'

with open('Python/students2.csv','a') as file:
    writer =   csv.DictWriter(file,fieldnames=['name', 'house'])
    writer.writerow({'name': name,'house':house})
    

'''
with open('Python/students2.txt','a') as file:
    writer =   csv.writer(file)
    writer.writerow([name,house])
    '''