from operator import itemgetter
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
#import imageio
#from wordcloud import WordCloud
#import wordcloud

blob = TextBlob(Path("bookofJohn.txt").read_text())
stops = stopwords.words("english")
more_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']
stops += more_stops

items = blob.word_counts.items()

clean_items = [i for i in items if i[0] not in stops]

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

top15 = sorted_list[:15]

new_top15 = ''

for i in top15:
        new_top15 += i[0] + ' '

print(new_top15)

'''
text = Path('book of John text.txt').read_text()
outfile = open('book of John text.txt', 'w')

wordcloud = WordCloud(colormap='prism', 
                      background_color='grey')

for line in text:
    if line not in line:
            line = line.replace(i, '')
        
outfile.write(line)

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("BOJ.png")

outfile. close()

print("done")
'''