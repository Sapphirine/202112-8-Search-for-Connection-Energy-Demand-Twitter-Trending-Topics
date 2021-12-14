from preprocess_tweets import tokenize_tweets
from load_tweets import *
from run_LDA import *
from visualize_LDA import *
import argparse


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--start_date', type=str, required=True)
    parser.add_argument('--end_date', type=str, required=True)
    parser.add_argument('--region', type=str, required=True)
    parser.add_argument('--tweet_directory', type=str, required=True)

    args = parser.parse_args()


    tweet_dataframe = load_tweets(args.tweet_directory)

    tokenized_dataframe = tokenize_tweets(tweet_dataframe)


    '''
    available regions: 
    ['longil','dunwod','hudvl','millwd','nyc',
    'capitl','north','genese','centrl','mhkvl','west']
    
    or 'all'
    '''
    filtered_dataframe = filter_dataframe(dataframe=tokenized_dataframe,
                                          start_date=args.start_date,
                                          end_date=args.end_date,
                                          region=args.region)

    LDA, bag_of_words = run_LDA(filtered_dataframe, num_topics=20)

    html_string = visualize_LDA_html(LDA, bag_of_words)

    html_file = open("lda.html", "w")
    html_file.write(html_string)
    html_file.close()



