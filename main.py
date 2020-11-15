import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import os

import numpy
from tensorflow.keras import Sequential
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import RMSprop

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import random
import json
import pickle
nltk.download('punkt')
import datetime

# import all the dependencies and libraries

with open("intents.json", encoding='utf-8') as file:
    data = json.load(file)
# open json file encoding it with utf-8
# try opening pickle files if present
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
# except if not present then run logic below
except:
    # these will be the tokenized words
    words = []
    # these will be the labels (intents)
    labels = []
    # appended list of tokenized sentences
    docs_x = []
    # intent tag for each pattern for an intent
    docs_y = []
    # we ignore the words that we don't require for our bot like ? and other strings
    ignore_words = ['?', ',', 'i', 'am', 'in', '"', '!', "'", 'I', '(', ')', "'s", 'a']
    # loop through each sentence in our intents patterns
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            # tokenize each word in the sentence
            wrds = nltk.word_tokenize(pattern)
            # add the tokenized words to the words list that was created
            words.extend(wrds)
            docs_x.append(wrds)
            # add the tokenized words to the doc_x that will be used for training
            docs_y.append(intent["tag"])
            # add the intent labels to doc_y to flag the intents later on
        if intent["tag"] not in labels:
            # Add the intent labels to the labels list
            labels.append(intent["tag"])
         # Remove ignored words from stemmed words
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    print(docs_x)
    # stem and lower each word and remove duplicates

    words = sorted(list(set(words)))

    # remove Duplicate intents

    labels = sorted(labels)

    training = []
    output = []

    # create an empty array full of 0 s based on the length of intent tags for our output that will be provided by the chatbot h.s s.a

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        ignore_words = ['?', ',', 'i', 'am', 'in', '"', '!', "'", 'a', 'I', 'to']
        # training set, bag of words for each sentence

        wrds = [stemmer.stem(w.lower()) for w in doc if w not in ignore_words]
        # based on the frequency of words in a tokenized pattern

        for w in words:
            if w in wrds:
                # create our bag of words array

                bag.append(1)
            else:
                bag.append(0)
        
        # output is a '0' for each tag and '1' for current tag
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# shuffle our features and turn into np.array
training = numpy.array(training)
print(training[0])
output = numpy.array(output)
print(output)
# create train and output array to be used for fitting the model
# Build neural network
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(len(training[0]),)))

model.add(Dense(64, activation="relu")) # 64 neurons first hidden hidden layer
model.add(Dense(64, activation="relu")) # 64 neurons second hidden layer
model.add(Dense(len(output[0]), activation="softmax")) # output layer number of neurons are total intents

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
# Defining the metrics
log_dir = "tensorflow_logs"
# create log folder
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1, write_graph=True)

# we are using the try and except conditions so that we don't re-run the entire file if model and pickle file are present
try:
    model = tf.keras.models.load_model("chatbot.h5")
except:
    history = model.fit(training,output, epochs=200, batch_size=20, callbacks=[tensorboard_callback])
    model.save("chatbot.h5")
# defining bag of words function for our chatbot so it can take the sentence and words and then bag them
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

# defining chat function that takes in the user input as the parameter and does the predictions
def chat(inp):
    print("Start talking with the bot!")
    results = model.predict(bag_of_words(inp, words).reshape(1,len(words)))[0]
    results_index = numpy.argmax(results) # argmax function in numpy helps in finding the index of the largest number in a vector
    tag = labels[results_index]
    if results[results_index]>0.50:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return(random.choice(responses))
    else:
        return("Sorry I didn't get you")

