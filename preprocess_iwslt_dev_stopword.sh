#!/bin/bash

# コーパスをtokenize/lowercaceした後vocabファイルを作り
# training, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus/IWSLT
ORIG_CORPUS=${CORPUS_DIR}/IWSLT17.TED

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess

YEAR="
2011
2012
2013
2014
2015
"

date

# extract sentence
tmp="
python ${PREP_DIR}/sentExt_iwslt_dev.py ${ORIG_CORPUS}.dev2010.en-ja.ja.xml \
                                        ${ORIG_CORPUS}.dev2010.en-ja.en.xml \
                                        ${CORPUS_DIR}/dev.iwslt.ext.ja \
                                        ${CORPUS_DIR}/dev.iwslt.ext.en 
"
for y in ${YEAR}
do
python ${PREP_DIR}/sentExt_iwslt_dev.py ${ORIG_CORPUS}.tst${y}.en-ja.ja.xml \
                                        ${ORIG_CORPUS}.tst${y}.en-ja.en.xml \
                                        ${CORPUS_DIR}/test${y}.iwslt.ext.ja \
                                        ${CORPUS_DIR}/test${y}.iwslt.ext.en 
done


# tokenize for japanese
tmp="
cat ${CORPUS_DIR}/dev.iwslt.ext.ja | mecab -Owakati | python3 han2zen.py \
                                   > ${CORPUS_DIR}/dev.iwslt.wakati.ja
"
for y in ${YEAR}
do
cat ${CORPUS_DIR}/test${y}.iwslt.ext.ja | mecab -Owakati | python3 han2zen.py \
                                        > ${CORPUS_DIR}/test${y}.iwslt.wakati.ja
done


# tokenize and lowercase
tmp="
cat ${CORPUS_DIR}/dev.iwslt.wakati.ja | python ${PREP_DIR}/tokenize_lowercase.py \
                                      > ${CORPUS_DIR}/dev.iwslt.tok.ja
cat ${CORPUS_DIR}/dev.iwslt.ext.en | python ${PREP_DIR}/tokenize_lowercase.py \
                                      > ${CORPUS_DIR}/dev.iwslt.tok.en
"
for y in ${YEAR}
do
cat ${CORPUS_DIR}/test${y}.iwslt.wakati.ja | python ${PREP_DIR}/tokenize_lowercase.py \
                                           > ${CORPUS_DIR}/test${y}.iwslt.tok.ja
cat ${CORPUS_DIR}/test${y}.iwslt.ext.en | python ${PREP_DIR}/tokenize_lowercase.py \
                                        > ${CORPUS_DIR}/test${y}.iwslt.tok.en
done


date
