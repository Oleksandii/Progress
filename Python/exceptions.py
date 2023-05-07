try:
    x = int(input('Write a number '))
    print(f'x is {x}')
except ValueError:
    print('It is not a number')
########
try:
    x = int(input('Write a number '))
    
except ValueError:
    print('It is not a number')
else:
    print(f'x is {x}')
################
try:
    x = int(input('Write a number '))
    
except ValueError:
    print('It is not a number')

print(f'x is {x}')
##################
try:
    x = int(input('Write a number '))   # same 3 last 
    
except ValueError:
    print('It is not a number')
else:
    return x
############
try:
    x = int(input('Write a number '))
    return x
except ValueError:
    print('It is not a number')

    
####################
try:
    return int(input('Write a number '))
    
except ValueError:
    print('It is not a number')

###########
try:
    x = int(input('Write a number '))   # same 3 last 
    
except ValueError:
    pass
else:
    return x
    
