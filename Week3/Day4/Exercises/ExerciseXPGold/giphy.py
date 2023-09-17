import requests

search_query = "hilarious" 
rating = "g" 
api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

url = f"https://api.giphy.com/v1/gifs/search?q={search_query}&rating={rating}&api_key={api_key}"

response = requests.get(url)

if response.status_code == 200: 
    gifs = response.json() 
    filtered_gifs = [gif for gif in gifs["data"]] 
    count = len(filtered_gifs) 
    print(f"Number of gifs with height bigger than 100: {count}") 
    print("The first 10 gifs:") 
    for gif in filtered_gifs[:10]: 
        print(gif["url"]) 
    else: 
        print("Error fetching gifs from Giphy API")