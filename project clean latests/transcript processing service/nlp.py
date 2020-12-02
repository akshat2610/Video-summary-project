'''
Inefficint version - just scratch work to see if everything works.
@author Akshat Bansal
'''
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import collections

TRANSCRIPT_PATH = 'C:\\project clean latests\\data\\uploaded\\transcript.txt'
DICTIONARY_PATH = 'C:\\project clean latests\\data\\uploaded\\dictionary.txt' 
DEFINE_PUNCTUATION_MARKS = ['.',',',';','!','%','\n','\r','�','-','=','(',')','[',']','@','+','?',"'", '"']

def map_sentences_timestamps():
    notes_timestamp_dict = collections.OrderedDict()
    try:
        transcript_file = open(TRANSCRIPT_PATH, 'r')
        keywords_file = open(DICTIONARY_PATH, 'r')

        transcript = transcript_file.read()
        tokenized_transcript = transcript.split('\n') 
        preprocessed_tokenized_transcript = preprocess_transcript(tokenized_transcript)

        keywords = keywords_file.read()
        tokenized_keywords = keywords.split(',') 

        stemmer = PorterStemmer()

        for i in range(0, len(preprocessed_tokenized_transcript)):
            text_line = preprocessed_tokenized_transcript[i]
            if is_timestamp(text_line):
                timestamp = text_line
                text = ''
                i += 1
                text_line = preprocessed_tokenized_transcript[i]
                while not is_timestamp(text_line) and i < len(preprocessed_tokenized_transcript):
                    text_line = preprocessed_tokenized_transcript[i]
                    if text_line == 'user avatar':
                        i += 2
                    else:
                        text += text_line
                        i += 1

                timestamp += '-' + text[len(text) - 8:]
                text = text[0: len(text) - 8]

                for keyword in tokenized_keywords:
                    if text.find(stemmer.stem(keyword)) != -1:
                        notes_timestamp_dict[text] = timestamp

    except Exception as e:
        print('Stress in mapping sentences to timestamps')
        print(e)

    finally:
        transcript_file.close()
        keywords_file.close()
        return notes_timestamp_dict


def preprocess_transcript(tokenized_transcript):
    transcript_punct_removed = remove_punct(tokenized_transcript)
    transcript_stopwords_removed = remove_stopwords(transcript_punct_removed)
    transcript_stemmed = stem_transcript(transcript_stopwords_removed)
   
    return transcript_stemmed

def remove_punct(tokenized_transcript):
    transcript_punct_removed = []

    for sentence in tokenized_transcript:
        sentence = sentence.lower()
        tokenized_sentence = sentence.split('\n')
        sentence_punct_removed = ''

        for word in tokenized_sentence:
            sentence_punct_removed += remove_word_punct(word)

        transcript_punct_removed.append(sentence_punct_removed)

    return transcript_punct_removed


def remove_stopwords(transcript_punct_removed):
    return transcript_punct_removed


def stem_transcript(transcript_stopwords_removed):
    stemmed_transcript = []
    stemmer = PorterStemmer()

    for sentence in transcript_stopwords_removed:
        tokenized_sentence = sentence.split('\n')
        stemmed_sentence = ''

        for word in tokenized_sentence:
            stemmed_sentence += stemmer.stem(word)

        stemmed_transcript.append(stemmed_sentence)

    return stemmed_transcript


def remove_word_punct(word):
    no_punct_form = ''
    for letter in word:
        if letter not in DEFINE_PUNCTUATION_MARKS:
            no_punct_form += letter
    return no_punct_form


def is_timestamp(text_line):
	return text_line.find(':') != -1
