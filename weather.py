import requests
degree_sign = u'\N{DEGREE SIGN}'
key = [Enter Key]

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

def calc_data(day, numOfHours, r):
    temp = []
    time = []
    weatDesc = []
    for x in range(0,numOfHours):
        temp.append(r.json()['data']['weather'][day]['hourly'][x]['tempF']+'    ')
        time.append(r.json()['data']['weather'][day]['hourly'][x]['time'])
        weatDesc.append(r.json()['data']['weather'][day]['hourly'][x]['weatherDesc'][0]['value'])
    return(temp, time, weatDesc)

def get_input():
    loc = input("Enter location: ")
    days = input("Enter number of days for forecast: ")
    return(loc, days)

def api_fetch(key, loc, days):
    r = requests.get("https://api.worldweatheronline.com/free/v2/weather.ashx?key="+key+"&q="+loc+"&num_of_days="+days+
                     "&format=json")
    return r

def cur_cond(r):
    curTemp = r.json()['data']['current_condition'][0]['temp_F']
    desc =  r.json()['data']['current_condition'][0]['weatherDesc'][0]['value']
    windSpd = r.json()['data']['current_condition'][0]['windspeedMiles']
    windDegree = r.json()['data']['current_condition'][0]['winddirDegree']
    visibility = r.json()['data']['current_condition'][0]['visibility']
    precip = r.json()['data']['current_condition'][0]['precipMM']
    code = r.json()['data']['current_condition'][0]['weatherCode']
    time = r.json()['data']['current_condition'][0]['observation_time']

    return(curTemp, desc, windSpd, windDegree, visibility, precip, code, time)

def print_curr(current, loc):
    print(loc)
    print("Current Conditions")
    print(current.desc)
    print("Observation Time: "+ current.time+ " "+"UTC")
    print(current.curTemp+''+degree_sign+'F')
    print("Wind "+current.windDegree+degree_sign)
    print("Wind Speed: "+current.windSpd+' '+"mph")
    print(current.visibility+' '+'mi')
    print(current.precip+' '+'in')

def print_forecast(days, r):
    #Outer loop to iterate through forecasted days
    #Inner loop called in function to iterate through hours per day
    for y in range(0, int(days)):

        numOfHours = len(r.json()['data']['weather'][y]['hourly'])
        temp, time, weatDesc = calc_data(y, numOfHours, r)
        date = r.json()['data']['weather'][y]['date']
        print("-----------------------------------------")
        print(loc)
        print("Forecast for "+date)
        print('{:10}{:10}{:10}'.format("Time", "Temp", "Weather Description"))
        for row in zip(time, temp, weatDesc):
            print('{:10}{:10}{:10}'.format(*row))
        print("-----------------------------------------")


if __name__ == "__main__":
    loc, days = get_input()
    r = api_fetch(key, loc, days)
    curTemp, desc, windSpd, windDegree, visibility, precip, code, cur_time= cur_cond(r)
    current = CurrWthr(curTemp, desc, windSpd, windDegree, visibility, precip, code, cur_time)
    print_curr(current, loc)
    print_forecast(days, r)






