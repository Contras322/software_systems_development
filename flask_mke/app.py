import json

from flask import Flask, render_template

from mke.routes import mke_app

app = Flask(__name__)

app.register_blueprint(mke_app, url_prefix='/mke')


app.config['DB_CONFIG'] = json.load(open('configs/db.json', 'r'))
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
def index():
    return render_template('base.html')


if (__name__ == "__main__"):
    app.run(host="127.0.0.1", port=9000, debug=True)