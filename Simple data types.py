name = input('Write your name ')#' ,.David Malone,.  '
name = ''

name = name.strip()#',.David Malone,.'   can strip().title()
name = name.strip(',.')#'David Malone'
name = name.lower() #'david malone'
name = name.capitalize()#'David malone'
name = name.upper()#'DAVID MALONE'
name = name.title()#'David Malone'
first, last = name.split(' ')# ' first = Devid , last = Malone'

x = input('x')
y = input('y')
z = float(x) +  float(y)

print(round(z))# x**2 , square(x), pow(x,2)

print(first)

print('Heloo',name, sep = '||',end='\t')
print('Hello '+ name )
print(f'Hello {name}!')





