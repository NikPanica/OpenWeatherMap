import pyowm

print('OpenWeatherMap')

own = pyowm.OWM('f9e71c31201382ffd16ebf549e93390f')
observation = own.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

translate = ('Rostov-na-Donu: Ростов-на-Дону', 'Moscow: Москва')

def WhatIsCloudness():
    if 0 <= weather.get_clouds() <=10:
        return 'ясная'
    if 10 < weather.get_clouds() <=30:
        return 'немного облачная'
    if 30 < weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 < weather.get_clouds() <=100:
        return 'мрачная'
print('Погода в городе' + ' ' + WhatIsCloudness() + ', температура ' + str(weather.get_temperature('celsius')['temp']) + ' градусов цельсия ' + 'скорость ветра ' + str(weather.get_wind()['speed']) + 'м/с.')

