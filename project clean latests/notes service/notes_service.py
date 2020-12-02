from flask import *
import os
import requests
from werkzeug.utils import secure_filename

TRANSCRIPT_UPLOAD_DESTINATION = 'C:\\project clean latests\\data\\uploaded\\transcript.txt'
DICTIONARY_UPLOAD_DESTINATION = 'C:\\project clean latests\\data\\uploaded\\dictionary.txt'

app = Flask(__name__)

@app.route('/')
def upload_transcript():
    return render_template("upload_form.html")

@app.route('/success', methods = ['POST'])
def success():
    f = request.files['transcript']
    f.save(TRANSCRIPT_UPLOAD_DESTINATION)
    f = request.files['dictionary']
    f.save(DICTIONARY_UPLOAD_DESTINATION)

    return redirect('http://127.0.0.1:8000/get_timestamps')


if __name__ == '__main__':
    app.run(port=3030)
