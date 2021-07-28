ARXIV_TAR = evm-metering.tar

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
	@echo '\pdfoutput=1' > arxiv/main.tex
	@echo nohypertex > arxiv/00README.XXX
	@sed -e 's/\\usepackage{xfp}//' main.tex >> arxiv/main.tex
	@cp IEEEtran.cls arxiv/
	@python replace_fpeval.py 'sections/*.tex' arxiv/
	@cp figures/*.pdf arxiv/figures
	@cp build/main.bbl arxiv
	@cd arxiv && tar cvf ../$(ARXIV_TAR) .

arxiv_submission: $(ARXIV_TAR)

.PHONY: build
