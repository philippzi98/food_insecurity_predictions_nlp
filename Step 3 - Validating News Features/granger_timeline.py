import pandas as pd
import datetime as dt
from datetime import datetime
import numpy as np
from sklearn.preprocessing import StandardScaler
import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree
from nltk.stem import PorterStemmer
from datetime import date

tag = 'word2vec-timeline'

from argparse import ArgumentParser

arguments = ArgumentParser()
arguments.add_argument('--word', type=str, default="famine")
arguments.add_argument('--phrase_file', type=str, default="news_phrases")
args = arguments.parse_args()

countries = ['AFGH', 'ANGOL', 'BURUN', 'CAFR', 'CAMER', 'CHAD', 'CONGO', 'ELSAL', 'ETHPA', 'GUAT', 'GUREP', 'HAIT', 'HON', 'KENYA', 'LIBER', 'MALAG', 'MALAW', 
    'MALI', 'MAURTN', 'MOZAM', 'NIGEA', 'NIGER', 'RWANDA', 'SENEG', 'SILEN', 'SOMAL', 'SOUSUD', 'SUDAN', 'TADZK', 'TAI', 'TANZA', 'UGANDA', 'UPVOLA', 'YEMAR',
    'ZAIRE', 'ZAMBIA', 'ZIMBAB']


base_dir = '/scratch/ab7325/Factiva/extraction-v11/avro/'
extract_id = 'oocuc4om6m'
phrases_file = '/scratch/ab7325/frame-models/logs/{}.csv'.format(args.phrase_file)
word = args.word

print (word, phrases_file)

w_df = {'date': [], word: [], 'country': []}
for t in range(25):
    df = pd.read_csv("{}/{}-{}.csv".format(base_dir, extract_id, str(t).zfill(5)))
    for r in df.iterrows():
        if len(word.split()) > 0:
            exists = True
            for w in word.split():
                if w not in stopwords.words('english'):
                    exists = exists and re.search(w, str(r[1]['body']), re.IGNORECASE)
        if re.search(word, str(r[1]['body']), re.IGNORECASE) or exists:
            for region in r[1]['region_codes'].split(','):
                if region.upper() in countries:
                    w_df['date'].append(r[1]['publication_datetime'])
                    w_df[word].append(1)                
                    w_df['country'].append(region.upper())
print(word, len(w_df['country']))
w_df['date'] = [dt.datetime.fromtimestamp(i/1000) for i in w_df['date']]
wc_df = pd.DataFrame.from_dict(w_df)
wc_df = wc_df.groupby('country').resample('MS', on='date').sum()
wc_df = wc_df.reset_index()
wc_df.fillna(0, inplace=True)
wc_df.to_csv('/scratch/ab7325/frame-models/logs/{}/{}.csv'.format(args.phrase_file, args.word))

