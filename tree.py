import os
from nltk.parse import stanford

parser = stanford.StanfordParser()
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print(sentences)

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()
