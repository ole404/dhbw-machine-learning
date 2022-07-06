from flask import Flask, request, jsonify, render_template
import transformers
import pandas as pd
from pymongo import MongoClient, collection
from pymongo.common import BaseObject
import bson
import os
import re
from dotenv import load_dotenv
load_dotenv('.env')

BOS_SEQUENCE = '<|elontweet|>'
app = Flask(__name__)
#init db connection
client = MongoClient(os.environ.get('DBCONN'))
pairs: collection = client.musktweets.pairs
guesses: collection = client.musktweets.guesses
#load model
model = transformers.TFGPT2LMHeadModel.from_pretrained('../musk/gpt2musk')
gen = transformers.pipeline('text-generation', model, tokenizer=transformers.AutoTokenizer.from_pretrained('../musk/musktokenizer'))

url_re = re.compile(r"https?:\/\/\S*")


#load dataset
data = pd.read_csv('./preprocessed_data/preprocessed_data_with_links.csv')
real_tweets = data['tweet']

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/tweet')
def get_tweet_db():
    raw_pair = list(pairs.aggregate([{"$sample": { "size": 1 }}]))[0]

    pair = {
        'id': str(raw_pair['_id']),
        'generated': raw_pair['generated'],
        'real': raw_pair['real']
    }
    print (pair)
    return jsonify(
        pair
    )

def get_tweet_gen():
    raw_generated = ""
    while (len(raw_generated) == 0):
        raw_generated = gen(BOS_SEQUENCE)[0]['generated_text'].lstrip(BOS_SEQUENCE)
    generated = url_re.sub("<link>", raw_generated)
    pair = {
        'generated': generated,
        'real': real_tweets.sample(n=1).values[0]
    }
    iOresult = pairs.insert_one(pair)
    pair['id'] = iOresult.inserted_id.__str__()
    del pair['_id']
    print(pair)
    return jsonify(
        pair
    )


@app.post('/guess')
def guess():
    print("well fuck?")
    req = request.json
    guesses.insert_one(req)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=80)

vote = {
    'id': 'id',
    'guess': ['faketweet', 'realtweet'],
}