#!/bin/dash
grep -iE '\|M$'| cut -d '|' -f3,3 | cut -d ',' -f1| sort | uniq