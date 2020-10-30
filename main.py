import os
import data
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello_world():
    return data.get_data('Weehee94')


if __name__ == '__main__':
    app.run()
