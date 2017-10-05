#!/bin/bash

# コーパスをtokenize/lowercaceした後vocabファイルを作り
# training, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus/ASPEC

PARTS="
train-1
train-2
train-3
dev
devtest
test
"

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess

NUM=1000
BEGIN=1

date

# extract sentence
sh sentExt_aspec.sh

# tokenize for japanese
for p in ${PARTS}
do
    cat ${CORPUS_DIR}/${p}.aspec.ja | mecab -Owakati | python3 han2zen.py > ${CORPUS_DIR}/${p}.aspec.wakati.ja
done

# tokenize and lowercase
for p in ${PARTS}
do
    cat ${CORPUS_DIR}/${p}.aspec.wakati.ja | python ${PREP_DIR}/tokenize_lowercase.py \
                                    > ${CORPUS_DIR}/${p}.aspec.tok.ja
    cat ${CORPUS_DIR}/${p}.aspec.en | python ${PREP_DIR}/tokenize_lowercase.py \
                                    > ${CORPUS_DIR}/${p}.aspec.tok.en
done


# make vocab file
TRAIN="
train-1
train-2
train-3
"
for l in ${SLAN} ${TLAN}
do
    echo -n > ${CORPUS_DIR}/train-all.aspec.${l}
    for f in ${TRAIN}
    do
        cat ${CORPUS_DIR}/${f}.aspec.tok.${l} >> ${CORPUS_DIR}/train-all.aspec.tok.${l}
    done
done

T=3
for l in ${SLAN} ${TLAN}
do
    cat ${CORPUS_DIR}/train-all.aspec.tok.${l} | python ${PREP_DIR}/count_freq.py ${T} \
                                               > ${CORPUS_DIR}/train.aspec.tok.${l}.vocab_t${T}_tab
done

# head vocab file
TOP_N=20000
for l in ${SLAN} ${TLAN}
do
    python ${PREP_DIR}/headVocab.py ${CORPUS_DIR}/train.aspec.tok.${l}.vocab_t${T}_tab ${TOP_N} > ${CORPUS_DIR}/train.aspec.tok.${l}.h${TOP_N}.vocab_t${T}_tab
done

date
