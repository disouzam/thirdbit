JEKYLL=bundle exec jekyll
SITE=./_site

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*.html)
LAYOUTS=$(wildcard _layouts/*.html)
POSTS=$(wildcard _posts/*/*.md)
PAGES=\
	atom.xml\
	$(wildcard *.html)\
	$(wildcard */index.md)\
	$(wildcard archive/*.html)\
	bib/index.html\
	blog/index.html\
	talks/speaking.md
STYLES=$(wildcard _sass/*/*.scss) $(wildcard css/*.css) $(wildcard css/*.scss)

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build:
	${JEKYLL} build

## serve: build site and run server
serve:
	${JEKYLL} serve

## drafts: build site and run server showing drafts
drafts:
	${JEKYLL} serve --future --drafts

## ----

## validate: check the generated HTML
validate:
	@html5validator --root _site \
	--blacklist browsercast btt dragnet js4ds mrsp sdxjs sdxpy \
	--ignore \
	'An "img" element must have an "alt" attribute' \
	'Attribute "align" not allowed' \
	'Attribute "label" not allowed on element "span"' \
	'The "align" attribute' \
	'The "bgcolor" attribute' \
	'The "border" attribute' \
	'The "cellpadding" attribute' \
	'The "font" element' \
	'The "strike" element is obsolete.' \
	'The "tt" element is obsolete.' \
	'The "valign" attribute' \
	'The "valign" attribute'

## links: check links in published site
links:
	linkchecker -F text https://third-bit.com > LINKS.txt

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}
