#!/bin/bash

MODULUS=$1
STEPCOUNT=$2
UKKOHOST=`python /Users/otteheinavaara/Desktop/HIITS15/running_utils/ukko_finder.py`
echo -n $UKKOHOST >> "$HOME/Desktop/randomCodes/supereven/runtmp.txt"