#!/bin/bash

declare -a files=("words.txt" "test.txt")

for f in "${files[@]}"; do
    echo "File: ${f}"


    cat "${f}"          `#read file` \
    | tr -s '[:space:]' `#remove repeated spaces, tabs and newlines` \
    | tr ' ' '\n'       `#change single spaces to newline` \
    | tr -s '\n'        `#remove excess newlines` \
    | sort              `#sort words (required for uniq call)` \
    | uniq -c           `#show only uniq occurencies with counters` \
    | sort -rg          `#sort in reverse order by numeric counters (form: 'counter' 'word')` \
    | awk '{ print $2 " " $1 }' # print in form: 'word' 'counter'

    echo -en "\n"
done
