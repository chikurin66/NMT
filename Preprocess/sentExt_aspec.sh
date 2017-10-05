#!/bin/bash

# ASPECのコーパスを.jaと.enに分割する


CORPUS_DIR=/home/takebayashi/src/corpus/ASPEC
CORPUS="
test
devtest
dev
train-1
train-2
train-3
"

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess


date

for f in ${CORPUS}
do
    echo -n > ${CORPUS_DIR}/${f}.aspec.${SLAN}
    echo -n > ${CORPUS_DIR}/${f}.aspec.${TLAN}

    python sentExt_aspec.py ${CORPUS_DIR}/${f}.txt \
                            ${CORPUS_DIR}/${f}.aspec.${SLAN} \
                            ${CORPUS_DIR}/${f}.aspec.${TLAN} 
    
done
