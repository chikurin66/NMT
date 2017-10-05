#!/bin/bash

# コーパスをtraining, dev, devtest, testに分ける

CORPUS_DIR=/home/takebayashi/src/corpus/news-commentary-v11
CORPUS=$CORPUS_DIR/news-commentary-v11.de-en

DEV_FILE=$CORPUS_DIR/dev.news-v11.de-en
DEVTEST_FILE=$CORPUS_DIR/devtest.news-v11.de-en
TEST_FILE=$CORPUS_DIR/test.news-v11.de-en
TRAIN_FILE=$CORPUS_DIR/train.news-v11.de-en

SLAN=de
TLAN=en

NUM=1000
BEGIN=1

date

for f in $DEV_FILE $DEVTEST_FILE $TEST_FILE
do
    cat $CORPUS.$SLAN | tail -n +$BEGIN | head -n $NUM > $f.$SLAN
    cat $CORPUS.$TLAN | tail -n +$BEGIN | head -n $NUM > $f.$TLAN
    BEGIN=`expr $BEGIN + $NUM`
done

cat $CORPUS.$SLAN | tail -n +$BEGIN > $TRAIN_FILE.$SLAN
cat $CORPUS.$TLAN | tail -n +$BEGIN > $TRAIN_FILE.$TLAN

