# Not Completed.


import random
import time
import requests

response = requests.get('https://testbooru.donmai.us/posts.json').json()
while True:
    time.sleep(2)
    p = random.randint(0, 19)
    print(p)
    print(response[p]['large_file_url'])
