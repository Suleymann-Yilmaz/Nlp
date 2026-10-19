import nltk
nltk.download("punkt")

text  = "Hello, World! How are you?"
word_tokens = nltk.word_tokenize(text)
print(word_tokens)
sent_tokens = nltk.sent_tokenize(text)
print(sent_tokens)


# Example sentences

ex_text = "Today, I was going to school. I saw Mehmet and ..."
word_tokens = nltk.word_tokenize(ex_text)
print(word_tokens)

sent_tokens = nltk.sent_tokenize(ex_text)
print(sent_tokens)