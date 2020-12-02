from flask import *
import requests
app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000)
