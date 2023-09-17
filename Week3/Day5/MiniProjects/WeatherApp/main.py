# import pyowm
# import matplotlib as mpl


# def get_info_weather_by_city(city):
#     owm = pyowm.OWM('eed88e9f82857b64e833b72b90d91480')
#     mgr = owm.weather_manager()

#     observation = mgr.weather_at_place(city)
#     city_weather = observation.weather
#     city_wind = city_weather.wind()
#     city_humidity = city_weather.humidity
#     city_sunrise_time = city_weather.sunrise_time(timeformat='iso')
#     city_sunset_time = city_weather.sunset_time(timeformat='iso')

#     print("Current weather in {city}:")
#     print("Temperature:", city_weather.temperature(unit='celsius')['temp'], "°C")
#     print("Wind speed:", city_wind["speed"], "m/s")
#     print("Wind direction:", city_wind["deg"], "degrees")
#     print("Sunrise time:", city_sunrise_time)
#     print("Sunset time:", city_sunset_time)
#     print("Humidity:", city_humidity, "%")

# get_info_weather_by_city('Tel Aviv, IL')
# get_info_weather_by_city(input("Type your city: \n"))

import pyowm 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
from datetime import datetime, timedelta 
import pytz

def init_plot(): plt.ylabel('Humidity (%)') 
plt.title('Three-day Humidity Forecast')

def plot_humidity(city): 
    owm = pyowm.OWM('eed88e9f82857b64e833b72b90d91480') 
    mgr = owm.weather_manager() 
    forecast = mgr.forecast_at_place(city, '3h')
    now = datetime.now()
    dates = []
    humidities = []
    for weather in forecast.forecast:
        forecast_time = weather.reference_time()
        forecast_time = datetime.fromtimestamp(forecast_time)
        if forecast_time >= now and forecast_time <= now + timedelta(days=3):
            date = forecast_time.strftime('%Y-%m-%d')
            humidity = weather.humidity
            dates.append(date)
            humidities.append(humidity)

    dates = [mdates.datestr2num(date) for date in dates]

    plt.bar(dates, humidities, width=0.5)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    write_humidity_on_bar_chart(humidities)

    plt.show()

def write_humidity_on_bar_chart(humidities): 
    for index, humidity in enumerate(humidities): 
        plt.text(index, humidity, f"{humidity}%", ha='center', va='bottom') 
    
init_plot()
plot_humidity('Tel Aviv')