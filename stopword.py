import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
print(stop_words)

text = "This is an example of removing stop word from text document."

filtered_text = [word for word in text.split() if word.lower() not in stop_words]
print(filtered_text)

stop_words_tr = set(stopwords.words("turkish"))
text = "Siz Bugün markete birkaç  ekmek almaya gittiniz."
lowered_text = text.lower()
not_stop = []

for word in lowered_text.split():
    if word not in stop_words_tr:
        not_stop.append(word)

print(text)
print(not_stop)