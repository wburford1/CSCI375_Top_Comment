import nltk
from classifier import Classifier
from collections import namedtuple

comment_sim = namedtuple('comment_sim', 'comment, similarity')

class CooccurranceClassifier(Classifier):
    def choose(self, c1, c2):
        c1_vector = {k.lower():0 for k in set(nltk.word_tokenize(c1))}
        c2_vector = {k.lower():0 for k in set(nltk.word_tokenize(c2))}
        sims1 = []
        sims2 = []
        for key in self.videos_dict:
            for comment in self.videos_dict[key]:
                if " " in comment.content:
                    com_tok = nltk.word_tokenize(comment.content)
                else:
                    # was getting a weird error with nltk if wasn't a senetence
                    com_tok = comment.content
                com_tok = [tok.lower() for tok in com_tok]
                for key in c1_vector:
                    if key in com_tok:
                        c1_vector[key] += 1
                for key in c2_vector:
                    if key in com_tok:
                        c2_vector[key] += 1

                sim1 = Classifier.cosine_similarity(list(c1_vector.values()), [1 for _ in range(0, len(c1_vector), 1)])
                sim2 = Classifier.cosine_similarity(list(c2_vector.values()), [1 for _ in range(0, len(c2_vector), 1)])

                if sim1 > 0: sims1.append(comment_sim(comment, sim1))
                if sim2 > 0: sims2.append(comment_sim(comment, sim2))

                for key in c1_vector:
                    c1_vector[key] = 0
                for key in c2_vector:
                    c2_vector[key] = 0
        sims1.sort(key=lambda tup: -1*tup[1])
        sims2.sort(key=lambda tup: -1*tup[1])
        cut_off = 0.75
        c1_tops = [com_sim.comment.likes for com_sim in sims1 if com_sim.similarity >= cut_off]
        c2_tops = [com_sim.comment.likes for com_sim in sims2 if com_sim.similarity >= cut_off]
        c1_likes = sum(c1_tops) / len(c1_tops) if len(c1_tops) > 0 else 0
        c2_likes = sum(c2_tops) / len(c2_tops) if len(c2_tops) > 0 else 0

        if c2_likes > c1_likes:
            conf = c1_likes / (c1_likes+c2_likes)
        else:
            conf = c2_likes / (c1_likes+c2_likes)

        return Classifier.classification(int(c2_likes>c1_likes), conf)
