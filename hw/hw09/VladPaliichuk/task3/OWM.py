from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(place: str):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp_date = w.temperature('celsius')
    
    rain_status = "Дощ" if w.rain else "Без дощу"
    
    weather_info = f"""
    Прогноз погоди {place}
    Небо: {w.detailed_status}
    Вітер: {w.wind().get('speed', 0)} м/с
    Вологість: {w.humidity} %
    Температура зараз: {temp_date['temp']} °C
    Макс / Мін темп: {temp_date['temp_max']} / {temp_date['temp_min']} °C
    Опади: {rain_status}
    Тепловий індекс: {w.heat_index if w.heat_index is not None else '—'} °C
    Хмарність: {w.clouds} %
    """
    return weather_info
    

get_weather("Lviv")