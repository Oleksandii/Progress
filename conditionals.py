'''
Construction:

if:
elif:
else:
'''
match name:
    case 'Harry'|'Hermione'|'Ron':
        print('Griffindor')
    case 'Drako':
        print('Slytherin')
    case _: 
        print('Who?')