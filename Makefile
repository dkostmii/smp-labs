DIAGRAM_THEME := vibrant
DOCS_MODULES := `echo domain.{action,runner,types} | tr " " "\n"`
DOCS_FILES := `echo domain.{action,runner,types}.html`

.PHONY: docs diagrams all

all: docs diagrams

docs:
	mkdir -p docs
	python -m pydoc -w $(DOCS_MODULES)
	mv -f $(DOCS_FILES) docs/

diagrams:
	plantuml docs/diagrams/src/*.pu -o ../out -theme $(DIAGRAM_THEME) -progress -duration -checkmetadata -tpng -failfast
