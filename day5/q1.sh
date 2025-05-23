#!/bin/dash

grep -E '^[^|]+/|1987/|'|cut -d "|" -f1|sort|uniq