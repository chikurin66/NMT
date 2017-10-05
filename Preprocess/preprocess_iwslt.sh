#!/bin/bash

# コーパスをtokenize/lowercaceした後vocabファイルを作り
# training, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus/IWSLT
ORIG_CORPUS=${CORPUS_DIR}/train.tags.en-ja
CORPUS=iwslt.tok

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess


date

# extract sentence

python sentExt_iwslt.py ${ORIG_CORPUS}.ja ${ORIG_CORPUS}.en \
                        ${CORPUS_DIR}/iwslt.ja ${CORPUS_DIR}/iwslt.en 

# tokenize for japanese
cat ${CORPUS_DIR}/iwslt.ja | mecab -Owakati | python3 han2zen.py > ${CORPUS_DIR}/iwslt.wakati.ja


# tokenize and lowercase
cat ${CORPUS_DIR}/iwslt.wakati.ja | python ${PREP_DIR}/tokenize_lowercase.py \
                                    > ${CORPUS_DIR}/iwslt.tok.ja
cat ${CORPUS_DIR}/iwslt.en | python ${PREP_DIR}/tokenize_lowercase.py \
                                    > ${CORPUS_DIR}/iwslt.tok.en


# make vocab file
TRAIN="
train-1
train-2
train-3
"

T=3
for l in ${SLAN} ${TLAN}
do
    cat ${CORPUS_DIR}/iwslt.tok.${l} | python ${PREP_DIR}/count_freq.py ${T} \
                                     > ${CORPUS_DIR}/iwslt.tok.${l}.vocab_t${T}_tab
done

# head vocab file
TOP_N=20000
for l in ${SLAN} ${TLAN}
do
    python ${PREP_DIR}/headVocab.py ${CORPUS_DIR}/iwslt.tok.${l}.vocab_t${T}_tab ${TOP_N} > ${CORPUS_DIR}/iwslt.tok.${l}.h${TOP_N}.vocab_t${T}_tab
done

date
