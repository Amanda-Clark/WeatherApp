codes = {
        '113': 'Sunny',
        '116': 'Partly Cloudy',
        '119': 'Cloudy',
        '122': 'Very Cloudy',
        '143': 'Fog',
        '176': 'Light Showers',
        '179': 'Light Sleet Showers',
        '182': 'Light Sleet',
        '185': 'Light Sleet',
        '200': 'Thundery Showers',
        '227': 'Light Snow',
        '230': 'Heavy Snow',
        '248': 'Fog',
        '260': 'Fog',
        '263': 'Light Showers',
        '266': 'Light Rain',
        '281': 'Light Sleet',
        '284': 'Light Sleet',
        '293': 'Light Rain',
        '296': 'Light Rain',
        '299': 'Heavy Showers',
        '302': 'Heavy Rain',
        '305': 'Heavy Showers',
        '308': 'Heavy Rain',
        '311': 'Light Sleet',
        '314': 'Light Sleet',
        '317': 'Light Sleet',
        '320': 'Light Snow',
        '323': 'Light Snow Showers',
        '326': 'Light Snow Showers',
        '329': 'Heavy Snow',
        '332': 'Heavy Snow',
        '335': 'Heavy Snow Showers',
        '338': 'Heavy Snow',
        '350': 'Light Sleet',
        '353': 'Light Showers',
        '356': 'Heavy Showers',
        '359': 'Heavy Rain',
        '362': 'Light Sleet Showers',
        '365': 'Light Sleet Showers',
        '368': 'Light Snow Showers',
        '371': 'Heavy Snow Showers',
        '374': 'Light Sleet Showers',
        '377': 'Light Sleet',
        '386': 'Thundery Showers',
        '389': 'Thundery Heavy Rain',
        '392': 'Thundery Snow Showers',
        '395': 'Heavy Snow Showers'
}
icons = {
'Unknown' : [
    "    .-.      ",
    "     __)     ",
    "    (        ",
    "     `-’     ",
    "      •      "
],
'Sunny': [
    "\033[38;5;226m    \\   /    \033[0m",
    "\033[38;5;226m     .-.     \033[0m",
    "\033[38;5;226m  ― (   ) ―  \033[0m",
    "\033[38;5;226m     `-’     \033[0m",
    "\033[38;5;226m    /   \\    \033[0m"
],
'Partly Cloudy' : [
    "\033[38;5;226m   \\  /\033[0m      ",
    "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "             "
],
'Cloudy' : [
    "             ",
    "\033[38;5;250m     .--.    \033[0m",
    "\033[38;5;250m  .-(    ).  \033[0m",
    "\033[38;5;250m (___.__)__) \033[0m",
    "             "
],
'Very Cloudy': [
    "             ",
    "\033[38;5;240;1m     .--.    \033[0m",
    "\033[38;5;240;1m  .-(    ).  \033[0m",
    "\033[38;5;240;1m (___.__)__) \033[0m",
    "             "
],
'Light Showers' : [
    "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
    "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"
],

'Heavy Showers': [
    "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
    "\033[38;5;21;1m   ‚‘‚‘‚‘‚‘  \033[0m",
    "\033[38;5;21;1m   ‚’‚’‚’‚’  \033[0m"
],

'Light Snow Showers' : [
    "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "\033[38;5;255m     *  *  * \033[0m",
    "\033[38;5;255m    *  *  *  \033[0m"
],
'Heavy Snow Showers' : [
    "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
    "\033[38;5;255;1m    * * * *  \033[0m",
    "\033[38;5;255;1m   * * * *   \033[0m"
],
'LightSleetShowers': [
    "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "\033[38;5;111m     ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m* \033[0m",
    "\033[38;5;255m    *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘  \033[0m"
],
'Thundery Showers' : [
    "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "\033[38;5;228;5m    ⚡\033[38;5;111;25m‘ ‘\033[38;5;228;5m⚡\033[38;5;111;25m‘ ‘ \033[0m",
    "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"
],
'Thundery Heavy Rain' : [
    "\033[38;5;240;1m     .-.     \033[0m",
    "\033[38;5;240;1m    (   ).   \033[0m",
    "\033[38;5;240;1m   (___(__)  \033[0m",
    "\033[38;5;21;1m  ‚‘\033[38;5;228;5m⚡\033[38;5;21;25m‘‚\033[38;5;228;5m⚡\033[38;5;21;25m‚‘   \033[0m",
    "\033[38;5;21;1m  ‚’‚’\033[38;5;228;5m⚡\033[38;5;21;25m’‚’   \033[0m"
],
'Thundery Snow Showers' : [
    "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
    "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
    "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
    "\033[38;5;255m     *\033[38;5;228;5m⚡\033[38;5;255;25m *\033[38;5;228;5m⚡\033[38;5;255;25m * \033[0m",
    "\033[38;5;255m    *  *  *  \033[0m"
],
'Light Rain' : [
    "\033[38;5;250m     .-.     \033[0m",
    "\033[38;5;250m    (   ).   \033[0m",
    "\033[38;5;250m   (___(__)  \033[0m",
    "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m",
    "\033[38;5;111m   ‘ ‘ ‘ ‘   \033[0m"
],
'Heavy Rain' : [
    "\033[38;5;240;1m     .-.     \033[0m",
    "\033[38;5;240;1m    (   ).   \033[0m",
    "\033[38;5;240;1m   (___(__)  \033[0m",
    "\033[38;5;21;1m  ‚‘‚‘‚‘‚‘   \033[0m",
    "\033[38;5;21;1m  ‚’‚’‚’‚’   \033[0m"
],
'Light Snow' : [
    "\033[38;5;250m     .-.     \033[0m",
    "\033[38;5;250m    (   ).   \033[0m",
    "\033[38;5;250m   (___(__)  \033[0m",
    "\033[38;5;255m    *  *  *  \033[0m",
    "\033[38;5;255m   *  *  *   \033[0m"
],
'Heavy Snow' : [
    "\033[38;5;240;1m     .-.     \033[0m",
    "\033[38;5;240;1m    (   ).   \033[0m",
    "\033[38;5;240;1m   (___(__)  \033[0m",
    "\033[38;5;255;1m   * * * *   \033[0m",
    "\033[38;5;255;1m  * * * *    \033[0m"
],
'Light Sleet' : [
    "\033[38;5;250m     .-.     \033[0m",
    "\033[38;5;250m    (   ).   \033[0m",
    "\033[38;5;250m   (___(__)  \033[0m",
    "\033[38;5;111m    ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m*  \033[0m",
    "\033[38;5;255m   *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘   \033[0m"
],
'Fog': [
    "             ",
    "\033[38;5;251m _ - _ - _ - \033[0m",
    "\033[38;5;251m  _ - _ - _  \033[0m",
    "\033[38;5;251m _ - _ - _ - \033[0m",
    "             "
]
}
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

loc = input("Enter location: ")
days = input("Enter number of days for forecast: ")
key = "7027bb81e4ded894671ebc09b8a9a"

def calc_data(days, numOfHours):
    for x in range(0,numOfHours):
        temp.append(r.json()['data']['weather'][0]['hourly'][x]['tempF'])
        time.append(r.json()['data']['weather'][0]['hourly'][x]['time'])
        weatDesc.append(r.json()['data']['weather'][0]['hourly'][x]['weatherDesc'][0]['value'])
    return(temp, time, weatDesc)

degree_sign= u'\N{DEGREE SIGN}'
import requests

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
temp = []
time = []
weatDesc = []

days = int(days)


icon = icons[codes[current.code]]
for line in icon:
    print(line)


print(loc)
print(current.desc)
print("Observation Time: "+ current.time+ " "+"UTC")
print(current.curTemp+''+degree_sign+'F')
print(current.windDegree)
print(current.windSpd+' '+"mph")
print(current.visibility+' '+'mi')
print(current.precip+' '+'in')




for y in range(0, int(days)):
    numOfHours = len(r.json()['data']['weather'][y]['hourly'])
    temp, time, weatDesc = calc_data(int(days), numOfHours)
    date = r.json()['data']['weather'][y]['date']
    print("-----------------------------------------")
    print(loc)
    print(date)
    for hour in time:
        print(hour, end=" ")
    print("\n")
    for degree in temp:
        print(degree, end=" ")
    print("\n")
    for weather in weatDesc:
        print(weather, end=" ")
    print("\n")
    print("-----------------------------------------")




