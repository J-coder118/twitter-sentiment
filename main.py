# Import Packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
import argparse
import time
import sys

parser = argparse.ArgumentParser(add_help=False, description=('Download tweets from Twitter'))
parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument('--keyword', '-k', help='Enter keyword to extract tweets')
args = parser.parse_args()

def twitter_sentiment_analyzer():
    """
    Collects tweets of the social-media content in Twitter when hashtag is given.
    :param tweets: Unique identification keyword for every social-media tweets in Twitter.
    :returns: Returns all the tweets.
    """
    analyser = SentimentIntensityAnalyzer()
    neu_sum, neg_sum, compound_sum, pos_sum, count = 0,0,0,0,0

    start_time = datetime.now()
    options = Options()
    options.headless = True
    options=options
    browser = webdriver.Chrome(options=options)
    browser.get("https://twitter.com/search?q=" + args.keyword)

    while browser.find_element_by_tag_name('div'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time_delta = datetime.now() - start_time
        sys.stdout.write('\r' + str(time_delta.seconds) + " seconds taken extract all the tweets" + '\r')
        sys.stdout.flush()
        if time_delta.seconds >= 120:
            break

    response = browser.page_source
    soup_obj = BeautifulSoup(response, 'lxml')
    #sys.stdout.write('\r' + "\n" + str(len(soup_obj.findAll('p', {'class' : 'TweetTextSize'}))) + '\r')
    #sys.stdout.flush()
    for item in soup_obj.findAll('p', {'class' : 'TweetTextSize'}):
        count += 1
        score = analyser.polarity_scores(item.text.replace('\n', '').strip())
        neu_sum += score['neu']
        neg_sum += score['neg']
        pos_sum += score['pos']

    if count:
        time.sleep(1)
        final_scores = {"neu" : round(neu_sum / count, 3), "neg" : round(neg_sum / count, 3), "pos" : round(pos_sum / count, 3), "compound" : round(compound_sum / count, 3)}
        browser.quit()
        return final_scores
    else:
        return None

if __name__ == '__main__':
    pol_scores = twitter_sentiment_analyzer()
    sys.stdout.write('\r' + 'Polarity Scores: ' + str(pol_scores)  + '\r')
    sys.stdout.flush()
