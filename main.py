# import requests
# from pprint import pprint
# from config import open_weather_token
#
#
# def get_weather(city, open_weather_token):
#     try:
#         r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
#         data = r.json()
#         #pprint(data)
#
#         city = data["name"]
#         weather = data["main"]["temp"]
#         wind = data["wind"]["speed"]
#         humidity = data["main"]["humidity"]
#
#         print(f"Погода в городе: {city}\nТемпература: {weather}\nСкорость ветра: {wind}\nВлажность: {humidity}")
#     except Exception as ex:
#         print(ex)
#         print(f"Проверь названия города {city}")
#
#
# def main():
#     city = input("Введите город: ")
#     get_weather(city, open_weather_token)
#
#
# if __name__== '__main__':
#     main()