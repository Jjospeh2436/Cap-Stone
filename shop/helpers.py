import decimal
import requests 
import requests_cache 
import json 
import random




#setup our api cache location (this is going to make a temporary database storage for our api calls)

requests_cache.install_cache('image_cache', backend='sqlite')


def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch/"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
        "X-RapidAPI-Key": "ca45dcf103msh0926f35e5311f97p1fe027jsnbaea78489632",
	    "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    # print(data)

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url

# def get_quote():
#     url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"

#     querystring = {"cat":"movies","count":"10"}

#     headers = {
# 	"X-RapidAPI-Key": "ca45dcf103msh0926f35e5311f97p1fe027jsnbaea78489632",
# 	"X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com"
# }
    
#     response = requests.post(url, headers=headers, params=querystring)

#     data = response.json()

#     return data

def get_quote():
    response = requests.get("https://type.fit/api/quotes")
    data = response.json()
    random_quote = data[random.randint(0, len(data) - 1)]["text"]
    return random_quote

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):  
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) 