import requests
degree_sign = u'\N{DEGREE SIGN}'

class CurrWthr(object):
    def __init__(self, *args):
        args = list(args)
        self.curTemp = args[0]
        self.desc = args[1]
        self.windSpd = args[2]
        self.windDegree = args[3]
        self.visibility = args[4]
        self.precip = args[5]
        self.code = args[6]
        self.time = args[7]

def calc_data(day, numOfHours):
    for x in range(0,numOfHours):
        temp.append(r.json()['data']['weather'][day]['hourly'][x]['tempF']+'    ')
        time.append(r.json()['data']['weather'][day]['hourly'][x]['time'])
        weatDesc.append(r.json()['data']['weather'][day]['hourly'][x]['weatherDesc'][0]['value'])
    return(temp, time, weatDesc)


loc = input("Enter location: ")
days = input("Enter number of days for forecast: ")
key = "7027bb81e4ded894671ebc09b8a9a"

forecast = dict()
r = requests.get("https://api.worldweatheronline.com/free/v2/weather.ashx?key="+key+"&q="+loc+"&num_of_days="+days+"&format=json")

curTemp = r.json()['data']['current_condition'][0]['temp_F']
desc =  r.json()['data']['current_condition'][0]['weatherDesc'][0]['value']
windSpd = r.json()['data']['current_condition'][0]['windspeedMiles']
windDegree = r.json()['data']['current_condition'][0]['winddirDegree']
visibility = r.json()['data']['current_condition'][0]['visibility']
precip = r.json()['data']['current_condition'][0]['precipMM']
code = r.json()['data']['current_condition'][0]['weatherCode']
time = r.json()['data']['current_condition'][0]['observation_time']

current = CurrWthr(curTemp, desc, windSpd, windDegree, visibility, precip, code, time)

days = int(days)

print(loc)
print("Current Conditions")
print(current.desc)
print("Observation Time: "+ current.time+ " "+"UTC")
print(current.curTemp+''+degree_sign+'F')
print("Wind "+current.windDegree+degree_sign)
print("Wind Speed: "+current.windSpd+' '+"mph")
print(current.visibility+' '+'mi')
print(current.precip+' '+'in')

#Outer loop to iterate through forecasted days
#Inner loop called in function to iterate through hours per day
for y in range(0, int(days)):
    temp = []
    time = []
    weatDesc = []
    numOfHours = len(r.json()['data']['weather'][y]['hourly'])
    temp, time, weatDesc = calc_data(y, numOfHours)
    date = r.json()['data']['weather'][y]['date']
    print("-----------------------------------------")
    print(loc)
    print("Forecast for "+date)
    print('{:10}{:10}{:10}'.format("Time", "Temp", "Weather Description"))
    for row in zip(time, temp, weatDesc):
        print('{:10}{:10}{:10}'.format(*row))
    print("-----------------------------------------")




