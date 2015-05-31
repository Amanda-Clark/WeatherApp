class CurrWthr(object):

    def __init__(self, *args):
        args = list(args)
        self.curTemp = args[0]
        self.desc = args[1]
        self.windSpd = args[2]
        self.windDegree = args[3]
        self.visibility = args[4]
        self.precip = args[5]


degree_sign= u'\N{DEGREE SIGN}'
import requests
key = "7027bb81e4ded894671ebc09b8a9a"
loc = "Fremont, CA"
days = "5"
r = requests.get("https://api.worldweatheronline.com/free/v2/weather.ashx?key="+key+"&q="+loc+"&num_of_days="+days+"&format=json")
r.text
r.json()
curTemp = r.json()['data']['current_condition'][0]['temp_F']
desc =  r.json()['data']['current_condition'][0]['weatherDesc'][0]['value']
windSpd = r.json()['data']['current_condition'][0]['windspeedMiles']
windDegree = r.json()['data']['current_condition'][0]['winddirDegree']
visibility = r.json()['data']['current_condition'][0]['visibility']
precip = r.json()['data']['current_condition'][0]['precipMM']

current = CurrWthr(curTemp, desc, windSpd, windDegree, visibility, precip)
print(loc)
print(current.desc)
print(current.curTemp+''+degree_sign+'F')
print(current.windDegree)
print(current.windSpd+' '+"mph")
print(current.visibility+' '+'mi')
print(current.precip+' '+'in')
