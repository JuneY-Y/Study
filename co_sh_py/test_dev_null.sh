#!/bin/dash
prefix="COP90445"
if echo "$prefix" | grep -E "[A-Z]{4}" >/dev/null; then
    echo "Match found."
else
    echo "No match."
fi