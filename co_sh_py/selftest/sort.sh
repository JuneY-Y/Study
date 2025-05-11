#!/bin/dash

## sort|uniq

cut -d '|' -f1 enrollments.txt | sort | uniq