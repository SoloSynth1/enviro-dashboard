from flask import Flask
from flask_apscheduler import APScheduler

from board import get_humidity, get_pressure, get_temperature, get_ambient_light
from db import insert_record


# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True


# initialize scheduler
scheduler = APScheduler()

# create app
app = Flask(__name__)
app.config.from_object(Config())


# cron examples
@scheduler.task('cron', id='record', minute='*')
def record():
    metrics = {
        'temperature': get_temperature,
        'humidity': get_humidity,
        'pressure': get_pressure,
        'ambient_light': get_ambient_light
    }
    for key, value in metrics.items():
        insert_record(key, value())


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()

