#!/bin/bash

dirname=$(dirname $0)
name=$1
input="$dirname/$name/$name.md"
output="$dirname/$name/$name.html"

options="--number-sections --toc"
options="$options --filter pandoc-citeproc"
options="$options --katex"

if [ ! -f "$input" ]; then
    echo "File not found!"
else
    options="$options --template $dirname/src/template.html"
    pandoc -i $input -o $output $options
fi