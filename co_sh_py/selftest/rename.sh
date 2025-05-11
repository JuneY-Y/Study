#!/bin/dash

awk -F'|' '{print $3 " " $4}' enrollments.txt|sort|uniq -d