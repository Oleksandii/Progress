'''
. - any character except newline
* - 0 or more repetitions
+ - 1 or more rep
? - 0 or 1 rep
{m} - m rep
{m,n} - m-n rep
^ - start
$ - end 
[] - set of charachters   [a-zA-Z0-9_ ]
[^] - complementing the set(except of sign)
\w - word character as well as digits and numbers and underscore == [a-zA-Z0-9_] without whitespaces
\W- not a word character 
\d - decimal digit = [0-9]
\D - not a decimal digit
\s - whitespace characters - space or tab
\S - not a whitespace
\- patterns
\.
A|B -(com|org|inc)- A or B
(...) - group
(?:...) - non-capturing version 

(\w|\s)==[a-zA-Z0-9_ ]

Flags:
    re.IGNORECASE
    re.MULTILINE
    re.DOTALL
search match fullmatch

'''
import re







email= input('What is your email? ')

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')
