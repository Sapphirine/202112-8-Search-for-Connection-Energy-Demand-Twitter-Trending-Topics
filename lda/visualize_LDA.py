import pyLDAvis.gensim

def visualize_LDA_html(tweets_lda, bag_of_words):
    vis = pyLDAvis.gensim.prepare(tweets_lda, bag_of_words, dictionary=tweets_lda.id2word)
    html_string = pyLDAvis.prepared_data_to_html(vis)

    return html_string

def visualize_LDA_notebook(tweets_lda, bag_of_words):
    pyLDAvis.enable_notebook()
    vis = pyLDAvis.gensim.prepare(tweets_lda, bag_of_words, dictionary=tweets_lda.id2word)
    return vis
