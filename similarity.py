from gensim.models.keyedvectors import KeyedVectors
from scipy.spatial.distance import euclidean
import numpy as np

# embeddings = KeyedVectors.load_word2vec_format('wiki-news-300d-1M-subword.vec', binary=False)
mu = 1/np.sqrt(2)


def sentence2vec(sentence):
    sentence = sentence.split()
    vecs = [embeddings[t] for t in sentence if t in embeddings]
    return np.mean(vecs)

def predicate_similarity(pred1, pred2):
    # e1 =sentence2vec(pred1)
    # e2 =sentence2vec(pred2)
    # dist = euclidean(e1, e2)
    # sim = np.exp(-dist/mu)
    # return sim
    return 0.5

def entity_similarity(ent1, ent2):
    # e1 =sentence2vec(ent1)
    # e2 =sentence2vec(ent2)
    # dist = euclidean(e1, e2)
    # sim = np.exp(-dist/mu)
    # return sim
    return 0.5

def tnorm(a, b):
    return a*b



