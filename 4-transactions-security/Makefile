ARXIV_TAR = transactional-throughput.tar

all: build

build:
	@latexmk -r .latexmkrc.local

clean:
	@latexmk -c

clean_arxiv_submission:
	@rm -rf arxiv
	@rm -f $(ARXIV_TAR)

$(ARXIV_TAR):
	@mkdir -p arxiv
	@mkdir -p arxiv/figures
	@mkdir -p arxiv/sections
	@mkdir -p arxiv/sections/tables
	@echo nohypertex > arxiv/00README.XXX
	@echo '\pdfoutput=1' > arxiv/main.tex
	@sed -e 's/\\usepackage{xfp}//' main.tex >> arxiv/main.tex
	@cp acmart.cls arxiv/
	@cp listingsgo.sty arxiv/
	@cp ACM-Reference-Format.* arxiv/
	@python replace_fpeval.py main.tex 'sections/**/*.tex' arxiv/
	@cp figures/*.pdf arxiv/figures
	@cp *.bib arxiv
	@cp build/main.bbl arxiv
	@cd arxiv && tar cvf ../$(ARXIV_TAR) .

arxiv_submission: $(ARXIV_TAR)

.PHONY: build $(ARXIV_TAR)
