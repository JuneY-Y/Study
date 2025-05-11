#!/bin/dash

## sort|uniq

awk -F'|' '{print $1}' enrollments.txt|sort|uniq
