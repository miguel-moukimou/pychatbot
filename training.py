import random
import json
import pickle
from xml.dom.minidom import Document
import numpy as np

import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.optimizers import gradient_descent_v2

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read()) 

words = []
classes = []
documents = []
ignore_letters = ['?', '!', ',','.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        elements_tupple = ((word_list), intent['tag'])
        documents.append(elements_tupple)
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)