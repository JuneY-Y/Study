#!/bin/dash
cut -d '|' -f3,4 enrollments.txt|sort|uniq -d