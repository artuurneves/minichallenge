import config
import requests
import json
import calendar


def get_weather(location):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location},br&appid={config.API_KEY}"
    r = requests.get(url=url, proxies=config.PROXIES)
    return r.content

def convert_fa_ce(kelvin):
    celcius = round(kelvin - 273.15, 2)
    return celcius


city = input('Cidade: ').replace(' ', '&nbsp')
result = get_weather(city)
c = json.loads(result)
weather = []
today = None
if c['message'] == 'city not found':
    print('Cidade não encontrada')
    quit()
for i in c['list']:
    list = {}
    if i['dt_txt'].split(' ')[0] != today:
        dow = calendar.weekday(int(i['dt_txt'].split(' ')[0].split('-')[0]), int(i['dt_txt'].split(' ')[0].split('-')[1]), int(i['dt_txt'].split(' ')[0].split('-')[2]))
        list = {'day': calendar.day_name[dow], 'temp_max': convert_fa_ce(i['main']['temp_max']), 'temp_min': convert_fa_ce(i['main']['temp_min'])}
        today = i['dt_txt'].split(' ')[0]
        weather.append(list)
for i in weather:
    print(i)
