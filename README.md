This folder is a git repository. If you don't want to use git (a version management tool), you can simply ignore this. 

# Computer labs for Evolution of Language and Music

Like this README, the labs are written in a mixture of markdown and latex. An overview of the markdown syntax can be found [here](https://daringfireball.net/projects/markdown/) (it's super easy). Pandoc is used to convert the files to PDF (under the hood, it first converts to latex, then uses PDFlatex to render the PDF). For convenience, each folder contains a makefile that builds the lab.

To build a pdf file:

```
cd lab-foo-bar/
make
```

The pdf file will be placed in a subfolder called 'build'.

This requires pandoc and a latex distribution to be installed. On ubuntu, this should suffice:

```
sudo apt-get install latexmk pandoc
```

For visual consistency, all labs import a bunch of commands from the file 'labs.tex'. This should be mostly self-explanatory. Furthermore, at the top of each lab, the different kinds bullet styles are explained. If you want to change any of this, it's recommended you do it in labs.tex.

# Suggested TODO

* add a makefile target to build the uploadable zip file for the lab (build the pdf, put in in a zip file together with the materials folder)
* add a master makefile in the root dir to build all labs 

# Notes per lab

## Lab 1

Not all files in the materials folder are used in the lab. When generating the zip file to upload to blackboard, check which ones are actually used in 

## Lab 2

## Lab 3

## Lab 4

## Lab 5
