import random
import statistics
import sys# need impoting for selfmade modules too
import cowsay
import requests
import json

if len(sys.argv)<2:
    sys.exit('too few argument')

response = requests.get('https.......ter='+sys.argv[1])
print(json.dumps(response.json(),indent = 2))





'''
####################
print(cowsay.cow('SSSSS'))
print(cowsay.dragon('sssss'))



#############################

for arg in sys.argv[1:]:
    print('Hello', arg)


#################################
if len(sys.argv)<2:
    sys.exit('too few argument')
elif len(sys.argv)>2:
    sys.exit('too many arguments')
print('Hello '+ sys.argv[1])

print(statistics.mean([100,90]))
#####################################

coin = random.choice(['A','B'])
number = random.randint(1,10)

cards = ['Queen','King','Jack']
random.shuffle(cards)


print(cards)
print(number)
print(coin)
'''