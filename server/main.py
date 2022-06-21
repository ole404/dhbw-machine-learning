from flask import Flask, request, jsonify, render_template
import transformers
import pandas as pd
from pymongo import MongoClient, collection
from pymongo.common import BaseObject
import bson
import os
from dotenv import load_dotenv
load_dotenv('.env')

BOS_SEQUENCE = '<|elontweet|>'
app = Flask(__name__)
#init db connection
client = MongoClient(os.environ.get('DBCONN'))
pairs: collection = client.musktweets.pairs
guesses: collection = client.musktweets.guesses
##load model
#model = transformers.TFGPT2LMHeadModel.from_pretrained('./gpt2musk')
#gen = transformers.pipeline('text-generation', model,)
##load dataset
data = pd.read_csv('./preprocessed_data/preprocessed_data.csv')
real_tweets = data['tweet']

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/tweet')
def get_tweet():
    pair = {
    #    'generated': gen(BOS_SEQUENCE).lstrip(BOS_SEQUENCE),
        'real': real_tweets.sample(n=1).values[0]
    }
    mockpair = {
        'real': real_tweets.sample(n=1).values[0],
        'generated': "I don't talk in actual tweets"
    }
    pair = mockpair
    iOresult = pairs.insert_one(pair)
    pair['id'] = iOresult.inserted_id.__str__()
    del pair['_id']
    print(pair)
    return jsonify(
        pair
    )


@app.post('/guess')
def guess():
    req = request.json
    guesses.insert_one(req)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()

vote = {
    'id': 'id',
    'guess': ['faketweet', 'realtweet'],
}