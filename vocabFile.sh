#!/bin/bash

CORPUS_DIR=/home/takebayashi/src/corpus/news-commentary-v11
CORPUS=$CORPUS_DIR/news-commentary-v11.de-en


T=3;
for f in $CORPUS.en $CORPUS.de 
do
    echo ${f}
    cat ${f} | python count_freq.py ${T} > $CORPIS_DIR/${f}.vocab_t${T}_tab
done
