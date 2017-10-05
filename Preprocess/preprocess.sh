#!/bin/bash

# コーパスをtokenize/lowercaceした後vocabファイルを作り
# training, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus
ORIG_CORPUS=${CORPUS_DIR}/news-commentary-v11/news-commentary-v11.de-en
CORPUS=${CORPUS_DIR}/news-commentary-v11.de-en.tok/news-commentary-v11.de-en.tok

SLAN=de
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess

NUM=1000
BEGIN=1

date


# tokenize and lowercase
cat ${ORIG_CORPUS}.${SLAN} | python ${PREP_DIR}/tokenize_lowercase.py > ${CORPUS}.${SLAN}
cat ${ORIG_CORPUS}.${TLAN} | python ${PREP_DIR}/tokenize_lowercase.py > ${CORPUS}.${TLAN}


# make vocab file
T=3
cat ${CORPUS}.${SLAN} | python ${PREP_DIR}/count_freq.py ${T} > ${CORPUS}.${SLAN}.vocab_t${T}_tab
cat ${CORPUS}.${TLAN} | python ${PREP_DIR}/count_freq.py ${T} > ${CORPUS}.${TLAN}.vocab_t${T}_tab

TOP_N=20000
python ${PREP_DIR}/headVocab.py ${CORPUS}.${SLAN}.vocab_t${T}_tab ${TOP_N} > ${CORPUS}.${SLAN}.h${TOP_N}.vocab_t${T}_tab
python ${PREP_DIR}/headVocab.py ${CORPUS}.${TLAN}.vocab_t${T}_tab ${TOP_N} > ${CORPUS}.${TLAN}.h${TOP_N}.vocab_t${T}_tab



# separate into 4 parts
DEV_FILE=${CORPUS_DIR}/news-commentary-v11.de-en.tok/dev.news-commentary-v11.de-en.tok
DEVTEST_FILE=${CORPUS_DIR}/news-commentary-v11.de-en.tok/devtest.news-commentary-v11.de-en.tok
TEST_FILE=${CORPUS_DIR}/news-commentary-v11.de-en.tok/test.news-commentary-v11.de-en.tok
TRAIN_FILE=${CORPUS_DIR}/news-commentary-v11.de-en.tok/train.news-commentary-v11.de-en.tok

for f in $DEV_FILE $DEVTEST_FILE $TEST_FILE
do
    cat ${CORPUS}.${SLAN} | tail -n +${BEGIN} | head -n ${NUM} > ${f}.${SLAN}
    cat ${CORPUS}.${TLAN} | tail -n +${BEGIN} | head -n ${NUM} > ${f}.${TLAN}
    BEGIN=`expr ${BEGIN} + ${NUM}`
done

cat ${CORPUS}.${SLAN} | tail -n +${BEGIN} > ${TRAIN_FILE}.${SLAN}
cat ${CORPUS}.${TLAN} | tail -n +${BEGIN} > ${TRAIN_FILE}.${TLAN}

