from utils.data import *

corpus_dir = '../Data/formatted'
corpus_pkl = corpus_dir + '/corpus_pkl.pkl'

# Read in the corpus
corpus = Corpus.get_corpus(corpus_dir, corpus_pkl)