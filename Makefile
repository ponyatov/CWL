CWD    = $(CURDIR)
MODULE = $(notdir $(CWD))

NOW = $(shell date +%d%m%y)
REL = $(shell git rev-parse --short=4 HEAD)

install: bin/python doc

bin/python:
	python3 -m venv .
	bin/pip3 install -U pip
	bin/pip3 install -U ply

WGET = wget -c

.PHONY: doc
doc: doc/TigerC.pdf doc/LittleSmalltalk.pdf

doc/TigerC.pdf:
	$(WGET) -O $@ https://doc.lagout.org/programmation/C/Modern%20Compiler%20Implementation%20in%20C%20%5BAppel%201997-12-13%5D.pdf

doc/LittleSmalltalk.pdf:
	$(WGET)	-O $@ http://sdmeta.gforge.inria.fr/FreeBooks/LittleSmalltalk/ALittleSmalltalk.pdf

.PHONY: merge release

MERGE  = Makefile README.md .gitignore
MERGE += $(MODULE).py

merge:
	git checkout master
	git checkout shadow -- $(MERGE)

release:
	git tag $(NOW)-$(REL)
	git push -v && git push -v --tags
	git checkout shadow
