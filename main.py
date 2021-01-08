#import gpt here
import gpt_2_simple as gpt2
import os
import requests
import tensorflow as tf
#flask setup here
from datetime import date
from flask import Flask, request
app = Flask(__name__)

#flask routes
def train():
    model_name = "355M"
    file_name = "data.txt"
    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess, file_name, model_name=model_name, steps=1000)
    return True

@app.route('/request/<model_name>/<generationCount>', methods=['GET'])
def generateXrequests(model_name, generationCount):
    generations = []
    for i in range(0, int(generationCount)):
        print(f'Generation count: {i}')
        tf.reset_default_graph()
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, run_name=model_name)
        generations.append(gpt2.generate(sess, return_as_list=True, run_name=model_name)[0])
    # form = {
    #     "created" : date.today(),
    #     "text" : " ".join(generations),
    #     "model" : model_name
    # }
    return f"<pre> {''.join(generations)} </pre>"

@app.route('/requestPre')
def loadPre():
    return 'preGeneratedRequests'

if __name__ == '__main__':
    askTrain = input('Enter [T (train) /R (run api)]: ')
    train() if askTrain.upper() == "T" else app.run(host= '0.0.0.0')