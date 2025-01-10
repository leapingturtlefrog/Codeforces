#!/bin/bash

PY_FILE_STRING="for m in range(int(input())):
    l = int(input())
    
    print()"

if [ $# -eq 1 ]; then
    mkdir "$1"
    cd "$1"
    for i in {1..7}; do
        touch "s$i.txt"
        echo "$PY_FILE_STRING" > "s$i.py"
    done
elif [ $# -gt 0 ]; then
    git add . || exit 1
    git commit -m "$*" || exit 2
    for dir in ./*; do
        if [ -d "$dir" ]; then
            for file in "$dir"/*; do
                if [ "$(cat "$file")" == "$PY_FILE_STRING" ]; then
                    rm "$file"
                elif [ ! -s "$file" ]; then
                    rm "$file"
                fi
            done
        fi
    done
fi