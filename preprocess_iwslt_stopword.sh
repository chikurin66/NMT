#!/bin/bash

# コーパスをtokenize/lowercaceした後vocabファイルを作り
# training, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus/IWSLT

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess

date


# delete stopword (top n from vocab) from training data
for f in "" "dev." "test2010." "test2011." "test2012." "test2013." "test2014." "test2015."
do
echo ${f}
python delete_stopword_iwslt.py \
    ${CORPUS_DIR}/iwslt.tok.ja.vocab_t3_tab ${CORPUS_DIR}/iwslt.tok.en.vocab_t3_tab \
    100 150 \
    ${CORPUS_DIR}/${f}iwslt.tok.ja ${CORPUS_DIR}/${f}iwslt.tok.en \
    ${CORPUS_DIR}/${f}iwslt.tok.noSW.ja ${CORPUS_DIR}/${f}iwslt.tok.noSW.en
done

date
