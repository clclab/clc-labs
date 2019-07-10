#!/bin/bash

dirname=$(dirname $0)
name=$1
input="$dirname/$name/$name.md"
output="$dirname/$name/$name.pdf"

options="--number-sections --number-offset=1 --toc"
options="$options --filter pandoc-citeproc"

if [ ! -f "$input" ]; then
    echo "File not found!"
else
    options="$options --template $dirname/src/template.tex"
    options="$options --lua-filter=src/texclass.lua" 
    pandoc $input -o $output $options

    # fls="$dirname/src/template.fls"
    # if [ ! -f "$fls" ]; then
    #   rm "$fls"
    # fi

    # log="$dirname/src/template.log"
    # if [ ! -f "$log" ]; then
    #   rm "$log"
    # fi

    # aux="$dirname/src/template.aux"
    # if [ ! -f "$aux" ]; then
    #   rm "$aux"
    # fi
    
fi