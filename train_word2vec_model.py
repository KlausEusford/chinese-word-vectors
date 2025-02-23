#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))


    inp = 'C:/Users/admin/Desktop/Chinsese_word_vectors-master/train.utf8'
    outp1 = 'C:/Users/admin/Desktop/Chinsese_word_vectors-master/wiki.zh.text.traditional.character.vec'
    outp2 = 'C:/Users/admin/Desktop/Chinsese_word_vectors-master/word_vector.txt'

    model = Word2Vec(LineSentence(inp), size=300, window=5, min_count=5,
            workers=multiprocessing.cpu_count(), iter=3)

    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
    print('OK')

