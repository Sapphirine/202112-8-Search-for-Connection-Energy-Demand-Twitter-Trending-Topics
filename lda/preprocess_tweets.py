import re
import gensim
from nltk.corpus import stopwords, wordnet
import nltk
from nltk.stem import WordNetLemmatizer

punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'

def tokenize_and_lemmatize(tweet):
    result = []
    for token in gensim.utils.simple_preprocess(tweet):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
            result.append(WordNetLemmatizer().lemmatize(token, pos='v'))
    return result


def remove_unrecognized_words(tokenized_tweets):
    wpt = nltk.WordPunctTokenizer()
    recognized_words = []

    for tweet in tokenized_tweets:
        tokens = wpt.tokenize(tweet)
        if tokens:
            for token in tokens:
                if wordnet.synsets(token):
                    recognized_words.append(token)

    return recognized_words


def preprocess_tweet(tweet):

    # Remove Retweets
    tweet = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    #Remove Mentions
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)

    # Remove http links
    tweet = re.sub(r'http\S+', '', tweet)
    # Remove Bitly links
    tweet = re.sub(r'bit.ly/\S+', '', tweet)
    # remove other links
    tweet = tweet.strip('[link]')
    # remove picture links
    tweet = re.sub(r'pic.twitter\S+', '', tweet)

    # remove hashtags
    tweet = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)

    # Remove video
    tweet = re.sub('VIDEO:', '', tweet)
    # Remove audio
    tweet = re.sub('AUDIO:', '', tweet)

    # lower case
    tweet = tweet.lower()

    # Remove punctuation
    tweet = re.sub('[' + punctuation + ']+', ' ', tweet)
    # Remove double spacing
    tweet = re.sub('\s+', ' ', tweet)
    # Remove numbers
    tweet = re.sub('([0-9]+)', '', tweet)
    # Lemmatization and tokenization
    tweet_token_list = tokenize_and_lemmatize(tweet)
    # Remove unrecognized words by wordnet
    tweet = remove_unrecognized_words(tweet_token_list)
    return tweet


def tokenize_tweets(df):
    df['tokens'] = df.text.apply(preprocess_tweet)
    return df