MAIN  = slides
FIGURES_SLIDES = $(patsubst %.eps,%.pdf,$(wildcard ./figures/*.eps))
FIGURES_THESIS = $(patsubst %.eps,%.pdf,$(wildcard ../figures/*.eps))

MAKEFLAGS += "-j 2"
.PHONY: all softclean clean distclean

all: $(MAIN).tex $(FIGURES_SLIDES) $(FIGURES_THESIS)
	# Remove a bunch of cache possibly left from epspdf.
	rm -rf figures/luatex* ../figures/luatex*
	# Compile thesis.
	latexmk -pdf -pdflatex="pdflatex -halt-on-error" $(MAIN).tex

%.pdf: %.eps
	epspdf $<

softclean:
	rm -rf figures/luatex*
	find -iregex '.*\.\(bbl\|blg\|aux\|log\|lof\|lot\|loa\|out\|toc\|dvi\|fdb_latexmk\|fls\)$$' -type f -delete

clean: softclean
	find -iregex '.*\.\(synctex\|idx\|ilg\|ind\|nav\|snm\|vrb\)$$' -type f -delete
	
distclean: clean
	find . -name "*.pdf" -type f -delete
