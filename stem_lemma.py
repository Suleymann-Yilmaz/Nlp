import nltk
nltk.download("wordnet")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

words = ["runs","runner","running","ran","run","better","go","went"]

for word in words:
    print(f"{word} - Stemmed : {stemmer.stem(word)}")


from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()

lemmas = [lemma.lemmatize(word,pos = "v") for word in words]
print(lemmas)


word_list = ["takes","took","taken","take","hotel","read","reads","reading","writes","wrote","writing","written","book","books"]
stems = [stemmer.stem(word) for word in word_list]
lemmas = [lemma.lemmatize(word,pos = "v") for word in word_list]
print(stems)
print(lemmas)