#!/bin/bash

PY_FILE_STRING='for m in range(int(input())):
    l = int(input())
    
    print()'

if [ $# -eq 1 ]; then
    mkdir "$1"
    cd "$1"
    for i in {1..7}; do
        touch "s$i.txt"
        echo "$PY_FILE_STRING" > "s$i.py"
    done
else
    for dir in ./*; do
        if [ -d "$dir" ]; then
            for file in "$dir"/*; do
                if [ grep -q "$PY_FILE_STRING" "$file" ]; then
                    rm "$file"
                elif [ ! -s "$file" ]; then
                    rm "$file"
                fi
            done
        fi
    done
fi