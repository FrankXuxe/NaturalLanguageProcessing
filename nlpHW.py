from operator import itemgetter
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
import imageio
from wordcloud import WordCloud
import wordcloud
mask_image = imageio.imread("mask_rectangle.png")
blob = TextBlob(Path("book of John text.txt").read_text())
stops = stopwords.words("english")
more_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']
stops += more_stops

items = blob.word_counts.items()

clean_items = [i for i in items if i[0] not in stops]

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

top15 = sorted_list[:16]

new_top15 = ''

for i in top15:
        new_top15 += i[0] + ' '

print(top15)


text = Path('book of John text.txt').read_text()

wordcloud = WordCloud(colormap='winter', mask= mask_image,
                      background_color='grey')

wordcloud = wordcloud.generate(new_top15)

wordcloud = wordcloud.to_file("BOJ.png")

print("done")
