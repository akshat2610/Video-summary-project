import flask
from movie import gen_video_summary

app = flask.Flask('Some app')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    gen_video_summary()
    return "Video editing service"


app.run(port=8888)
