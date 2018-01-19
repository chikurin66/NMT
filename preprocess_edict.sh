#!/bin/bash


CORPUS_DIR=/home/takebayashi/src/corpus/EDICT
ORIG_CORPUS=${CORPUS_DIR}/IWSLT17.TED

SLAN=ja
TLAN=en

PREP_DIR=/home/takebayashi/src/Preprocess

YEAR=2010

date

# extract sentence
DONE="
cat ${CORPUS_DIR}/edict.txt \
    | python sentExt_edict.py ${PREP_DIR}/stopword.en \
    | python3 han2zen.py \
    | python split.py ${CORPUS_DIR}/edict.ext.ja ${CORPUS_DIR}/edict.ext.en

cat ${CORPUS_DIR}/edict.ext.ja | mecab -Owakati > ${CORPUS_DIR}/edict.wakati.ja

python delete_stopword.py ${PREP_DIR}/stopword.ja ${CORPUS_DIR}/edict.wakati.ja ${CORPUS_DIR}/edict.ext.en \
    ${CORPUS_DIR}/edict.tok.ja ${CORPUS_DIR}/edict.tok.en
"

N_OP=32000
CODE_FILE=${CORPUS_DIR}/shared_bpe${N_OP}.code
#cat ${CORPUS_DIR}/edict.tok.ja ${CORPUS_DIR}/edict.tok.en | python ./bpe/learn_bpe.py -s ${N_OP} -o ${CODE_FILE}

#python3 ./bpe/apply_bpe.py -c ${CODE_FILE} < ${CORPUS_DIR}/edict.tok.ja | python3 ./bpe/get_vocab.py > ${CORPUS_DIR}/edict.tok.vocab.ja
#python3 ./bpe/apply_bpe.py -c ${CODE_FILE} < ${CORPUS_DIR}/edict.tok.en | python3 ./bpe/get_vocab.py > ${CORPUS_DIR}/edict.tok.vocab.en

python3 ./bpe/apply_bpe.py -c ${CODE_FILE} < ${CORPUS_DIR}/edict.tok.ja > ${CORPUS_DIR}/edict.bpe.ja
python3 ./bpe/apply_bpe.py -c ${CODE_FILE} < ${CORPUS_DIR}/edict.tok.en > ${CORPUS_DIR}/edict.bpe.en
