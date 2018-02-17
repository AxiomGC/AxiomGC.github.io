import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
nltk.download()
from nltk.corpus import stopwords

train = pd.read_csv("labeledTrainData.tsv", header=0, \
                    delimiter="\t", quoting=3)


example1 = BeautifulSoup(train["review"][0])
letters_only = re.sub("[^a-zA-Z]",
                      " ",
                      example1.get_text())
#print(letters_only)

lower_case = letters_only.lower()
words = lower_case.split()
words = [w for w in words if not w in stopwords.words("english")]
print(words)
