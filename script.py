import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text = "This is a simple sentence."
tokens = word_tokenize(text)
print(tokens)