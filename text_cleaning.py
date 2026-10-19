"""
NLP Pipeline:

1 - Data Collection
2 - Text Cleaning
    1 -) Text Cleaning
    2 -) Tokenization
    3 -) Stemming and Lemmatization
    4 -) Stop words
3 - Preprocessing
4 - Modelling
5 - Evaluating
6 - Deployment

"""

sentence = "Hello,        World!     2"
cleaned_text = " ".join(sentence.split())
print(sentence,"-",cleaned_text)

text = "HELLO World!"
cleaned_text_2 = text.lower()
print(cleaned_text_2)

import string

text = "Hello, world! 2023."
cleaned_text_3 = text.translate(str.maketrans("","",string.punctuation))
print(cleaned_text_3)

text = "Today! is, a great day..."
cleaned_text_4 = text.translate(str.maketrans("","",string.punctuation))
print(cleaned_text_4)

import re

text = "Hello,   World! 2035"
cleaned_text_5 = re.sub(r"[^A-Za-z0-9\s]","",text)
print(cleaned_text_5)


from textblob import TextBlob

text = "Helıo, wırld! 2035"
cleaned_text_6 = str(TextBlob(text).correct())
print(cleaned_text_6)


"""from bs4 import BeautifulSoup
text = "<div> Hello, world! 2035</div>"
cleaned_text_7 = BeautifulSoup(text,"html_parser").get_text()
print(cleaned_text_7)"""



# Examples
ex_text = "Hi, how are     you?"
cleaned_ex_text = " ".join(ex_text.split())
print(cleaned_ex_text)

ex_text = "Hi, how are you?"
cleaned_ex_text_2 = ex_text.lower()
print(cleaned_ex_text_2)

cleaned_ex_text_3 = ex_text.translate(str.maketrans("","",string.punctuation))
print(cleaned_ex_text_3)

ex_text = "Hi, how are% you#?"
cleaned_ex_text_4 = re.sub(r"[^A-Za-z0-9\s]","",ex_text)
print(cleaned_ex_text_4)

ex_text = "Hello, how ari yoe?"
cleaned_ex_text_5 = TextBlob(ex_text).correct()
print(cleaned_ex_text_5)