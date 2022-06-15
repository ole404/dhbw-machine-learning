from flask import Flask, request, jsonify
import transformers
import pandas as pd
from pymongo import MongoClient, collection
from pymongo.common import BaseObject
import bson


BOS_SEQUENCE = '<|elontweet|>'
app = Flask(__name__)
#init db connection
client= MongoClient()
pairs:collection = client.musktweets.pairs
guesses:collection = client.musktweets.guesses
##load model
model = transformers.TFGPT2LMHeadModel.from_pretrained('./gpt2musk')
gen = transformers.pipeline('text-generation', model,)
##load dataset
data = pd.read_csv('./preprocessed_data/tweets')
real_tweets = data['tweets']
@app.get('/tweet')
def get_tweet():
    pair = {
        'real': gen(BOS_SEQUENCE).lstrip(BOS_SEQUENCE),
        'generated': real_tweets.sample(n=1).values[0]
    }
    mockpair

    iOresult = pairs.insertOne(pair)
    pair['id'] = iOresult.inserted_id
    return jsonify(
        pair
    )
app.post('/guess')
def post():
    req = request.json
    guesses.insertOne(req)

vote = {
    'id': 'id',
    'guess': ['faketweet', 'realtweet'],
}