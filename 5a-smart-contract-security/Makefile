ARXIV_TAR = smart-contracts-vulnerabilities.tar

all: build

build:
	@latexmk -r .latexmkrc.local

clean_arxiv_submission:
	@rm -rf arxiv
	@rm -f smart-contracts-vulnerabilities.tar

$(ARXIV_TAR): clean_arxiv_submission build
	@mkdir -p arxiv
	@mkdir -p arxiv/figures
	@mkdir -p arxiv/sections
	@mkdir -p arxiv/sections/tables
	@echo '\pdfoutput=1' > arxiv/main.tex
	@cat main.tex >> arxiv/main.tex
	@cp usenix.sty arxiv
	@cp sections/*.tex arxiv/sections
	@cp sections/tables/*.tex arxiv/sections/tables
	@cp solidity-highlighting.sty arxiv
	@cp figures/all.pdf arxiv/figures
	@cp figures/vulnerable.pdf arxiv/figures
	@cp figures/balance-histogram.pdf arxiv/figures
	@cp figures/cumulative-ether.pdf arxiv/figures
	@cp figures/overlap-analyzed.pdf arxiv/figures
	@cp figures/overlap-vulnerable.pdf arxiv/figures
	@cp build/main.bbl arxiv
	@cd arxiv && tar cvf ../$(ARXIV_TAR) .

arxiv_submission: $(ARXIV_TAR)

.PHONY: build
