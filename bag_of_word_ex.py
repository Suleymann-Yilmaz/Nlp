import re 
import string
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

data = pd.read_csv("IMDB.csv") # IMDB 50K Dataset
print(data.head(3)) 

comments = data["review"]
label = data["sentiment"]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+","",text)
    text = text.translate(str.maketrans("","",string.punctuation))
    text = [word for word in text.split() if word not in stop_words]
    text = [word for word in text if len(word)>2]
    text = " ".join(text)

    return text

cleaned_comment = [clean_text(comment) for comment in comments]
vectorizer = CountVectorizer()
sample = vectorizer.fit_transform(cleaned_comment[:100])

print(cleaned_comment[:5])

feature_names= vectorizer.get_feature_names_out()
print(feature_names)
print(sample.toarray()[:2])

data_bag = pd.DataFrame(sample.toarray(),columns = feature_names)
print(data_bag.head())


word_counts = sample.sum(axis = 0).A1
print(word_counts)

word_frequency = dict(zip(feature_names,word_counts))
print(word_frequency)

common_words = Counter(word_frequency).most_common(5)
print(common_words)