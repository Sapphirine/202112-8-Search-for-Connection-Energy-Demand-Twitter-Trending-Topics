import os
import json
import pandas as pd


def load_tweets(directory):
    dictList = []

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            data = json.load(f)
            if 'data' in data.keys():
                for tweet in data['data']:
                    tweet['region'] = filename[11:-5]
                dictList.append(data['data'])
    dicts = []
    for L in dictList:
        dicts += L

    df = pd.DataFrame(dicts)

    df['created_at'] = pd.to_datetime(df['created_at'])

    return df