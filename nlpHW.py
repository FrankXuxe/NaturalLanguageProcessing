from operator import itemgetter
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

blob = TextBlob(Path("book of John text.txt").read_text())
stops = stopwords.words("english")
