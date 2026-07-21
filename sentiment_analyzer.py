from textblob import TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "Relatable (Positive)"
    # Polarity is a number between -1 and 1
    else:
        return "Neutral/Mixed"