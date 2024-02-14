#!/usr/bin/bash
STREAM_JAR=$1
LOCAL_INP=$2
HDFS_INP=$3
HDFS_OUT=$4
FILES=$5

# put files on hdfs
hdfs dfs -rm -r ${HDFS_INP}example_input
hdfs dfs -mkdir -p ${HDFS_INP}example_input/
hdfs dfs -put ${LOCAL_INP} ${HDFS_INP}example_input/
hadoop jar $STREAM_JAR -input ${HDFS_INP}example_input/ -output $HDFS_OUT/example_output/ -mapper ${FILES}mapper -file ${FILES}mapper -reducer ${FILES}reducer -file ${FILES}reducer