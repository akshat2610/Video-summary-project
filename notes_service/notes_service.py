from flask import *
import requests
app = Flask(__name__)

@app.route('/')
def upload_transcript():
    return render_template("multiple_upload_form.html")

'''
@app.route('/upload_dictionary')
def upload_dictionary():
    if request.method == 'POST':
        f = request.files['file']
        f.save('C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\upload folder\\' + f.filename)
'''


@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['transcript']
        f.save('C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\upload folder\\transcript\\transcript.txt')
        f = request.files['dictionary']
        f.save('C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\upload folder\\dictionary\\dictionary.txt')

        return requests.get('http://127.0.0.1:8000/get_timestamps').text



if __name__ == '__main__':
    app.run(port=3030)
