import requests
# from pprint import pprint
import datetime
from config import API_key


def getting_the_weather(city):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric')
        data = r.json()
        # pprint(data)
        dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"{dt_now}\nГород: {data['name']}\nТемпература: {data['main']['temp']}°С\n" \
               f"Ощущается: {data['main']['feels_like']}\n" \
               f"Влажность воздуха: {data['main']['humidity']}%\nСкорость ветра: {data['wind']['speed']} м/с\n"
    except KeyError:
        return 'Проверьте название города!'


def main():
    city = input('Введите город: ')
    print(getting_the_weather(city))


if __name__ == '__main__':
    main()
