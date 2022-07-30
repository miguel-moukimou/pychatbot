from audioop import reverse
from pyexpat import model
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.python.keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read()) 

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.model')

def clean_sentence_up(sentence):
    sentence_of_words = nltk.word_tokenize(sentence)
    sentence_of_words = [lemmatizer.lemmatize(word) for word in sentence_of_words]
    return sentence_of_words


def convert_to_bag_of_words(sentence):
    sentence_of_words = clean_sentence_up(sentence)
    bag = [0] * len(words)
    for wrd in sentence_of_words:
        for i, word in enumerate(words):
            if word == wrd:
                bag[i] = 1
    return np.array(bag)

def class_prediction(sentence):
    bag_of_words = convert_to_bag_of_words(sentence)
    result = model.predict(np.array([bag_of_words]))[0]
    ERROR_THRESHOLD = 0.25
    end_result = [[i,r] for i,r in enumerate(result) if r > ERROR_THRESHOLD] 

    end_result.sort(key=lambda x: x[1], reverse=True)
    return_list = []   
    for r in end_result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def process_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('Ready, waiting for user input')

while True:
    message = input('')
    ints = class_prediction(message)
    res = process_response(ints, intents)
    print(res)