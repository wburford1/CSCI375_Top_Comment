# abstract class for a general classifier
from collections import namedtuple

class Classifier:
    classification = namedtuple('classification', 'choice, confidence')

    def __init__(self, videos_dict):
        self.videos_dict = videos_dict

    # should return 0 if c1, 1 if c2 and a confidence packaged in the classification namedtuple
    def choose(self, c1, c2, video_id):
        raise NotImplementedError

    @staticmethod
    def cosine_similarity(vector1, vector2):
        assert len(vector1) == len(vector2)
        dot_prod = sum([vector1[i]*vector2[i] for i in range(0, len(vector1), 1)])
        mag1_squared = sum([vector1[i]**2 for i in range(0, len(vector1), 1)])
        mag2_squared = sum([vector2[i]**2 for i in range(0, len(vector2), 1)])
        if mag1_squared == 0 or mag2_squared == 0:
            return 0
        return dot_prod / ((mag1_squared * mag2_squared)**(1/2))
