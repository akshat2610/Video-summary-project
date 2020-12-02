import flask
import requests

app = flask.Flask('Some app')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    transcript_request = requests.get('http://127.0.0.1:8000/')
    video_editing_request = requests.get('http://127.0.0.1:5000/')
    return "Transcript service response: " + str(transcript_request.text) + "\nVideo editing service response: " + str(video_editing_request.text)


app.run(port=8080)
