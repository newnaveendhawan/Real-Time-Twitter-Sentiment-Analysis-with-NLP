from flask import Flask, render_template, request
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import os
from dotenv import load_dotenv
import time

load_dotenv()
app = Flask(__name__)

bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=bearer_token)

analyzer = SentimentIntensityAnalyzer()

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"@\w+", "", tweet)
    tweet = re.sub(r"#\w+", "", tweet)
    return tweet.strip()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return ("Positive", compound)
    elif compound <= -0.05:
        return ("Negative", compound)
    else:
        return ("Neutral", compound)

@app.route("/", methods=["GET", "POST"])
def index():
    tweets_data = []
    username = ""
    error = None
    sentiment_summary = {"Positive": 0, "Negative": 0, "Neutral": 0}
    total_tweets = 0

    if request.method == "POST":
        username = request.form.get("username")
        if username:
            username = username.strip()
            try:
                user = client.get_user(username=username)
                if user and user.data:
                    user_id = user.data.id
                    tweets = client.get_users_tweets(id=user_id, max_results=10, tweet_fields=["created_at"])

                    if tweets.data:
                        for tweet in tweets.data:
                            cleaned = clean_tweet(tweet.text)
                            sentiment = analyze_sentiment(cleaned)
                            tweets_data.append((cleaned, sentiment, tweet.created_at.strftime("%Y-%m-%d %H:%M")))
                            sentiment_summary[sentiment[0]] += 1
                            total_tweets += 1
                            time.sleep(1.5)

                        for key in sentiment_summary:
                            sentiment_summary[key] = round((sentiment_summary[key] / total_tweets) * 100, 2)
                else:
                    error = "User not found."
            except Exception as e:
                error = str(e)
        else:
            error = "Username is required."

    return render_template("index.html",
                           tweets=tweets_data,
                           username=username,
                           error=error,
                           summary=sentiment_summary,
                           total=total_tweets)

if __name__ == "__main__":
    app.run(debug=True)
