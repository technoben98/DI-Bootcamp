import requests
import time

def request_time(url):
    start_request = time.time()
    r = requests.get(url)
    after_request = time.time()
    load_time = after_request - start_request
    return f"'{url}' load time is {load_time}."

print(request_time("https://www.google.co.il/"))
print(request_time("https://www.ynet.co.il/"))
print(request_time("https://www.imdb.com"))