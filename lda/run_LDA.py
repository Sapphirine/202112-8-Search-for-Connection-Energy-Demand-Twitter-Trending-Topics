
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel


def filter_dataframe(dataframe, start_date, end_date, region):

    region_list = ['longil','dunwod','hudvl','millwd','nyc',
    'capitl','north','genese','centrl','mhkvl','west', 'all']
    if region not in region_list:
        raise Exception('Invalid Region')

    df = dataframe.loc[(dataframe.created_at >= start_date)
                       & (dataframe.created_at < end_date)].sort_index()


    if len(df) == 0:
        raise Exception('No tweets in date range')

    if region != 'all':
        df = df.loc[(df.region == region)]

    if len(df) == 0:
        raise Exception('region does not exist in date range')
    return df


def run_LDA(dataframe, num_topics):
    text_dict = Dictionary(dataframe.tokens)
    tweets_bow = [text_dict.doc2bow(tweet) for tweet in dataframe['tokens']]
    k = num_topics
    tweets_lda = LdaModel(tweets_bow,
                          num_topics=k,
                          id2word=text_dict,
                          random_state=2,
                          passes=10,
                          iterations=100)

    return tweets_lda, tweets_bow
