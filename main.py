from operator import truediv
from flask import Flask, render_template, request
from astral.sun import sun
from astral import LocationInfo
import datetime

app = Flask(__name__)


def is_day():
    now = datetime.datetime.now()
    city = LocationInfo("Moscow")
    s = sun(city.observer, date = datetime.datetime.now())
    if s["sunrise"].time() < now.time() < s["dusk"].time():
        return True
    else:
        return False


def calculate_suntimes():
    city = LocationInfo("Moscow")
    s = sun(city.observer, date = datetime.datetime.now())
    time_data = {
        'Sunrise': s["sunrise"].time().strftime("%H:%M:%S"),
        'Dusk': s["dusk"].time().strftime("%H:%M:%S")
    }
    if is_day():
        return time_data['Dusk']
    else:
        return time_data['Sunrise']






@app.route('/')
def home():
    suntimes = calculate_suntimes()
    obj = {
        'time_to': suntimes,
        'is_day': is_day(),
    }
    return render_template('homepage.html', times = obj)

app.run(host = '0.0.0.0', port = 88)