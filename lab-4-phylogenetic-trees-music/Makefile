BUILDDIR=build/

TEXFILES := $(patsubst %.md,%.tex,$(wildcard *.md))
PDFFILES := $(patsubst %.md,$(BUILDDIR)%.pdf,$(wildcard *.md))

all : $(PDFFILES)

$(BUILDDIR)%.tex : %.md
	pandoc $< -f markdown-all_symbols_escapable --standalone --smart -o $@

$(BUILDDIR)%.pdf : $(BUILDDIR)%.tex
	latexmk -pdf -output-directory=$(BUILDDIR) -pdflatex="pdflatex -interaction=nonstopmode" -use-make $< 
