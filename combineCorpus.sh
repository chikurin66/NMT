#!/bin/bash

CORPUS_DIR=/home/takebayashi/src/corpus
EDICT=${CORPUS_DIR}/EDICT/edict.tok
IWSLT=${CORPUS_DIR}/IWSLT/iwslt.tok
OUT=${CORPUS_DIR}/IWSLT-EDICT/iwslt-edict.tok


for l in ja en
do
    nkf -w ${EDICT}.$l > ${OUT}.$l
    nkf -w ${IWSLT}.$l >> ${OUT}.$l
done
