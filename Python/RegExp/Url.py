import re
url= input('your url').strip()




if matches := re.search(r'^(?:https?://)?(www\.)?twitter\.com/(\w+)$',"",url):
    print(f"Username: {matches.group(1)}")

username = url.sub(r'^(https?://)?(www\.)?twitter\.com/',"",url)# replacing 1 on 2 and writing in 3


username = url.replace('https://twitter.com/',"")
print(f'Username : {username}')
