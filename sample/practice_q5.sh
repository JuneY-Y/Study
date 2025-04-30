#!/bin/bash

file="$1"
grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++'