ARXIV_TAR = defi-leveraging.tar

all: build

build:
	@latexmk -r .latexmkrc.local

clean_arxiv_submission:
	@rm -rf arxiv
	@rm -f $(ARXIV_TAR)

$(ARXIV_TAR): clean_arxiv_submission build
	@mkdir -p arxiv
	@mkdir -p arxiv/figures
	@mkdir -p arxiv/sections
	@mkdir -p arxiv/tables
	@echo nohypertex > arxiv/00README.XXX
	@echo '\pdfoutput=1' > arxiv/main.tex
	@cat main.tex >> arxiv/main.tex
	@cp common.sty arxiv
	@cp llncs.cls arxiv/
	@cp sections/*.tex arxiv/sections
	@cp tables/*.tex arxiv/tables
	@cp figures/*.pdf arxiv/figures
	@cp build/main.bbl arxiv
	@tar -C arxiv -cvf $(ARXIV_TAR) .

arxiv_submission: $(ARXIV_TAR)

.PHONY: build
