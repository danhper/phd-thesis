import bibtexparser

parser = bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False)

with open("./bibliography.bib") as f:
    bib_database = bibtexparser.load(f, parser)

with open("./unused.txt") as f:
    unused = set(f.read().splitlines())


bib_database.entries = [
    entry for entry in bib_database.entries if entry["ID"] not in unused
]
writer = bibtexparser.bwriter.BibTexWriter()
writer.contents = ["entries"]
writer.indent = "  "


with open("bibliography_clean.bib", "w") as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file, writer)
