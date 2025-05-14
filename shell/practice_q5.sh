#!/bin/dash
## Find Years an Award Was Not Given

Award=$1
filename=$2

real_award=$(cut -d '|' -f1 $Award)
# echo "$real_award"