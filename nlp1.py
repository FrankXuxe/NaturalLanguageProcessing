from textblob import Word
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

#Chinese = blob.translate(to='zh')

# print(Chinese)

# print(Chinese.translate())


index = Word('index')

print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())


# WordList
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#spellcheck and correction
word = Word('theyr')

print(word.spellcheck())

print(word.correct())

# Normalization

word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())

# Definitions, Synonyms and Antonyms from WordNet
happy = Word("happy")
print(happy.definitions)

print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
