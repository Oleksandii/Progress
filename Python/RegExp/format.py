import re

name= input('What is your name? ').strip()



if matches := re.search(r"^.+, ?.+$",name):



if matches:
    last, first = matches.groups()
    name = f"{first} {last} "
    # or last = matches.group(1) first = matches.group(2) or name = matches.group(1)+ ' ' + matches.group(2)
print(f"Hello {name}")


if ',' in name:
    first,last = name.split(', ')
    name = f'{first} {last}'

print(f"Hello {name}")
