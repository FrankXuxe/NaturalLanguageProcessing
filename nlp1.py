from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer

text = "Today is a beautiful day. Tomorrow looks like a bad wheather."
text = ""

blob = TextBlob(text)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

# print(round(blob.sentiment.polarity, 3))
# print(round(blob.sentiment.subjectivity, 3))

# for sentence in blob.sentences:
#    print(sentence)
#    print(round(sentence.sentiment.polarity, 3))


#blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)

# for sentence in blob.sentences:
#    print(sentence.sentiment)

Chinese = blob.translate(to='zh')

print(Chinese)

print(Chinese.translate())