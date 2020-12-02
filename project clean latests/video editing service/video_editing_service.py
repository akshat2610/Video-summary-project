from flask import *
from movie import gen_video_summary

app = Flask('Some app')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    gen_video_summary()
    return render_template('playback.html')


app.run(port=8888)