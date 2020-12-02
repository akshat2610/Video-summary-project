import flask
from flask import Flask, redirect
import requests
from nlp import map_sentences_timestamps

app = flask.Flask('Some app')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Transcript processing service</h1>"

@app.route('/get_timestamps', methods=['GET'])
def get_timestamps():
    sentence_timestamp_dict = map_sentences_timestamps()
    timestamp_list = sentence_timestamp_dict.values()
    timestamp_str = '+'.join(timestamp_list)

    timestamp_file = open('C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\notes and timestamps data folder\\timestamp\\timestamp.txt', 'w')
    timestamp_file.write(timestamp_str)
    timestamp_file.close()

    return redirect('http://127.0.0.1:8888/', code = 301)




@app.route('/get_notes', methods=['GET'])
def get_notes_timestamp_dict():
    return map_sentences_timestamps()


if __name__ == '__main__':
    '''
    transcript_path = 'C:\\Work\\SJSU\\Fall 2020\\CS 160\\project\\summary service\\preprocessing\\sample transcript\\CS 149 lecture 1.txt'
    keywords_path = 'C:\\Work\\SJSU\\Fall 2020\\CS 160\\project\\summary service\\preprocessing\\sample transcript\\keywords.txt'
    notes_timestamp_dict = get_notes_timestamp_dict(transcript_path, keywords_path)
    print(notes_timestamp_dict)
    '''
    app.run(port=8000)
