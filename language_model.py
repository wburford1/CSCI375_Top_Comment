from collections import Counter, namedtuple
from math import log
import nltk

LanguageModel = namedtuple('LanguageModel', 'num_tokens, vocab, nminus1grams, ngrams') # holds counts for the lm
DELIM = "_" # delimiter for tokens in an ngram

def tokenize_text(text):
    """ Converts a string to a list of tokens """
    tokens = []
    for sent in nltk.sent_tokenize(text):
        sent_tokens = nltk.word_tokenize(sent)
        sent_tokens.insert(0,'<s>')
        sent_tokens.append('</s>')
        tokens.extend(sent_tokens)

    return tokens

def generate_ngrams(tokens, n):
    """ Returns a list of ngrams made from a list of tokens """
    ngrams = []
    if n > 0:
        for i in range(0, len(tokens)-n+1):
            ngrams.append(DELIM.join(tokens[i:i+n]))

    return ngrams

def build_lm(text, n):
    """ Builds an ngram language model. """
    tokens = tokenize_text(text)

    num_tokens = len(tokens)
    vocab = set(tokens)
    nminus1grams = Counter(generate_ngrams(tokens, n - 1))
    ngrams = Counter(generate_ngrams(tokens, n))

    return LanguageModel(num_tokens, vocab, nminus1grams, ngrams)

def laplace_log_prob(lm, token, history=None):
    """ Computes the probability of the ngram.

    Returns the Add-1 smoothed log-probability of 
    "token" following "history"

    Args:
        lm (LanguageModel): ngram counts from the corpus
        token: target token
        history: n-1 previous tokens or None

    Return:
        float: log-probability of the ngram
    """
    if history == None: #unigram model
        ngram_count = lm.ngrams.get(token, 0) + 1
        history_count = lm.num_tokens + len(lm.vocab)
    else:
        ngram_count = lm.ngrams.get(history+DELIM+token, 0) + 1
        history_count = lm.nminus1grams.get(history, 0) + len(lm.vocab)

    return log(float(ngram_count) / history_count)

if __name__ == '__main__':
    """ example usage"""

    with open("category_corpus.txt", 'r') as file:
        text = file.read()

    lm = build_lm(text, 2) #bigram model

    history = "<s>"
    probs = [(w,laplace_log_prob(lm, w, history)) for w in lm.vocab]
    print(probs)
    print("10 most probable words to follow '{}': {}".format(history, probs[:10]))

