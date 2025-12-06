# HW 09
# Task 3

from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather

# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75

# ---
def get_weather_info(place: str) -> dict:
    
    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather

        temp = w.temperature('celsius')  # dict with keys: temp, temp_min, temp_max
        wind = w.wind() or {}

        data = {
            "status": w.detailed_status or "N/A",
            "temp": temp.get("temp", "N/A"),
            "temp_min": temp.get("temp_min", "N/A"),
            "temp_max": temp.get("temp_max", "N/A"),
            "humidity": w.humidity if w.humidity is not None else "N/A",
            "wind_speed": wind.get("speed", "N/A"),
            "wind_deg": wind.get("deg", "N/A"),
            "clouds": w.clouds if w.clouds is not None else "N/A",
            "rain": w.rain if w.rain else {},
        }

        return {"ok": True, "data": data}
    except Exception as e:
        # return error string for caller to display / handle
        return {"ok": False, "error": str(e)}
# --- 

