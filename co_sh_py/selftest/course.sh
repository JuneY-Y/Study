#!/bin/dash

awk -F'|' '{print $3}' enrollments.txt | sort|uniq -c|awk '$1>=3 {print $0}'
