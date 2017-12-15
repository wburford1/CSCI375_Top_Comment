import random

class MarkovChain:

    def __init__(self):
        self.memory = {}

    def _learn_key(self, key, value):
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, text):
        tokens = text.split()
        bigrams = [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens) - 1)]
        for bigram in bigrams:
            self._learn_key(bigram[0], bigram[1])

    def _next(self, current_state):

        if not current_state:
            next_possible = self.memory.keys()
        else:
            if current_state[0] in self.memory:
                next_possible = self.memory.get(current_state[0])
            else:
                next_possible = self.memory.keys()

        return random.sample(next_possible, 1)

    def babble(self, amount, state=''):
        if not amount:
            return state

        next_word = self._next(state)
        return str(state) + ' ' + str(self.babble(amount - 1, next_word))

if __name__ == '__main__':
    m = MarkovChain()
    
    corpus = open("category_corpus.txt", 'r').read().splitlines()
    for c in corpus:
        m.learn(c)
        next = m.babble(random.randint(5, 20)).split()
        for n in next:
            length = len(n)-2
            print(n[2:length], end=' ')
        print("")

