import requests
import datetime

import time as ti

from datetime import datetime as dt2
from geopy.geocoders import Nominatim
from rich import print
from rich.layout import Layout
from rich.panel import  Panel
from rich.table import Table
from rich.text import Text

degree_sign = u'\N{DEGREE SIGN}'
key = ""


class CurrWthr(object):
    def __init__(self, *args):
        args = list(args)
        self.curTemp = args[0]
        self.desc = args[1]
        self.windSpd = args[2]
        self.windDegree = args[3]
        self.visibility = args[4]
        self.humidity = args[5]
        self.time = args[6]


def get_input():
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")

    return latitude, longitude


def api_fetch(apikey, latitude, longitude):
    result = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + latitude + "&lon="
                     + longitude + "&units=imperial&exclude=minutely,hourly&appid=" + apikey)
    return result


def cur_cond(r):
    curTemp = str(r.json()['current']['temp'])
    desc = r.json()['current']['weather'][0]['description']
    windSpd = str(r.json()['current']['wind_speed'])
    windDegree = str(r.json()['current']['wind_deg'])
    visibility = r.json()['current']['visibility']
    visibility = visibility / 1000
    visibility = str(visibility)
    humidity = str(r.json()['current']['humidity'])
    time = r.json()['current']['dt']
    time = str(dt2.utcfromtimestamp(time).strftime('%Y-%m-%d %H'))
    return curTemp, desc, windSpd, windDegree, visibility, humidity, time


def print_curr(current, layout):
    table = Table(expand=True)
    text = Text("Current Conditions")
    text.stylize("cyan")
    table.add_column(text, justify="center", no_wrap=True)
    table.add_row("Observation Time: " + current.time + " " + "UTC")
    table.add_row(current.curTemp + '' + degree_sign + 'F')
    table.add_row("Wind Direction: " + current.windDegree + degree_sign)
    table.add_row("Wind Speed: " + current.windSpd + ' ' + "mph")
    table.add_row(current.visibility + ' ' + 'kilometers visibility')
    table.add_row(current.humidity + ' ' + '% humidity')
    layout["current"].update(table)


def create_tables(layout, layouts):
    x=1
    for day in layouts:
        table = Table()

        layout[day].split(
            Layout(table)
        )
        x = x+1


def create_layout():
    cr_layout = Layout(name="root")
    cr_layout.split(
        Layout(name="header", size=4),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=20)
    )
    cr_layout["footer"].split_row(
        Layout(name="day1"),
        Layout(name="day2"),
        Layout(name="day3"),
        Layout(name="day4"),
        Layout(name="day5"),
        Layout(name="day6"),
        Layout(name="day7"),
        Layout(name="day8")
    )
    cr_layout["main"].split_row(
        Layout(name="alerts"),
        Layout(name="current"),
    )

    return cr_layout


def get_alerts(alerts):
    tbls =[]
    if len(alerts) < 3:
        for alert in alerts:
            table = Table()
            text = Text("Severe Weather Alerts")
            text.stylize("red")
            table.add_column(text, justify="center", no_wrap=True)
            table.add_row("Agency: "+alert['sender_name'], style="red")
            table.add_row("Event: " + alert['event'], style="red")
            start = dt2.utcfromtimestamp(alert['start']).strftime('%Y-%m-%d %H:%M:%S')
            end = dt2.utcfromtimestamp(alert['end']).strftime('%Y-%m-%d %H:%M:%S')
            table.add_row("Starts: " + start, style="red")
            table.add_row("Ends: " + end, style="red")
            table.add_row("Description: " + alert['description'], style="red")
            table.add_row(" ")
            table.add_row(" ")
            tbls.append(table)

    return tbls


def print_forecast(r, layout):

    x = 1
    for day in r.json()['daily']:
        dayofweek = ti.strftime('%A', ti.localtime(day['dt']))
        time = str(dt2.utcfromtimestamp(day["dt"]).strftime('%Y-%m-%d'))

        highTemp = str(day["temp"]["max"])
        lowTemp = str(day["temp"]["min"])

        sunrise = str(datetime.datetime.fromtimestamp(day['sunrise']).strftime('%H:%M:%S'))
        sunset = str(datetime.datetime.fromtimestamp(day['sunset']).strftime('%H:%M:%S'))
        desc = str(day['weather'][0]['description'])
        clouds = str(day['clouds'])
        humidity = str(day['humidity'])

        if 'alerts' in r.json():
            tbls = get_alerts(r.json()['alerts'])
            for tbl in tbls:
                layout["alerts"].update(tbl)
        else:
            table = Table()
            text = Text("No Severe Weather Alerts")
            text.stylize("green")
            table.add_column(text, justify="center", no_wrap=True)
            table.add_row("Agency: " + "", style="green")
            table.add_row("Event: " + "", style="green")
            table.add_row("Starts: " + "", style="green")
            table.add_row("Ends: " + "", style="green")
            table.add_row("Description: " + "", style="green")
            table.add_row(" ")
            table.add_row(" ")
            layout["alerts"].update(table)

        if 'rain' not in day:
            totrain = "N/A"
        else:
            totrain = str(day['rain'])+"mm"

        table = Table()
        text = Text(dayofweek + " "+time)
        text.stylize("cyan")
        table.add_column(text, justify="center",  no_wrap=True)
        table.add_row("")
        table.add_row("Low Temp: " + lowTemp+degree_sign)
        table.add_row("High Temp: " + highTemp+degree_sign)
        table.add_row("Humidity: " + humidity+ "%")
        table.add_row("Sunrise: " + sunrise, style="cyan")
        table.add_row("Barometric Pressure: "+str(day['pressure'])+" hPa")
        table.add_row("Wind Speed: " +str(day["wind_speed"])+" mph")
        table.add_row("Wind Direction: "+ str(day["wind_deg"])+degree_sign)
        table.add_row("Sunset: " + sunset)
        table.add_row(desc)
        table.add_row("Precip: " + totrain)
        table.add_row("Cloud cover: " + clouds + "%")
        table.add_row("")
        layout["day"+str(x)].split(
            Layout(table),
        )

        x = x+1


if __name__ == "__main__":
    layout = create_layout()
    lat, lng = get_input()
    r = api_fetch(key, lat, lng)
    curTemp, desc, windSpd, windDegree, visibility, humidity, time = cur_cond(r)
    current = CurrWthr(curTemp, desc, windSpd, windDegree, visibility, humidity, time)
    print_curr(current, layout)
    print_forecast(r, layout)

    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        "Latitude: "+ lat+ " Longitude: "+lng,
        dt2.now().ctime().replace(":", "[blink]:[/]"),
    )
    geolocator = Nominatim(user_agent="app")
    Latitude = lat
    Longitude = lng
    location = geolocator.reverse(Latitude + "," + Longitude)
    address = location.address
    grid.add_row("Current Weather and Forecast for "+ address)
    #grid.add_row(address)
    layout["header"].update(
        Panel(
            grid,
            style="white on blue",
        )
    )

    print(layout)
