LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rf
TMP_SUFFS   = pdf aux bbl blg log dvi ps eps out
CHECK_RERUN = grep Rerun $*.log

NAME = ms

all: ${NAME}.pdf

vc.tex: ../.git/logs/HEAD
	echo "%%% This file is generated by the Makefile." > vc.tex
	git log -1 --date=short --format="format:\\newcommand{\\githash}{%h}\\newcommand{\\gitdate}{%ad}\\newcommand{\\gitauthor}{%an}" >> vc.tex

${NAME}.pdf: ${NAME}.tex vc.tex
	${LATEX} ${NAME}
	bibtex ${NAME}
	( ${CHECK_RERUN} && ${LATEX} ${NAME} ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} ${NAME} ) || echo "Done."

clean:
	${RM} $(foreach suff, ${TMP_SUFFS}, ${NAME}.${suff})