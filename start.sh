#!/bin/bash

#mainly to debug locally
if [ -z $SERVICE_DIR ]; then export SERVICE_DIR=`pwd`; fi

rm -f finished

if [ $ENV == "IUHPC" ]; then
	module load python
fi

(
nohup time python $SERVICE_DIR/main.py > stdout.log 2> stderr.log 

if [ -s output.png ]
then 
    echo 0 > finished
else
    echo "output missing"
    echo 1 > finished
    exit 1
fi
) &