from flask import Flask

app = Flask(__name__)
app.config.from_object('app.etc.conf')


@app.route('/')
def index():
    print('a')
    return "index"
