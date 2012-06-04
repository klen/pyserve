PYTHON=$(CURDIR)/env/bin/python
PIP=$(CURDIR)/env/bin/pip

all: env dist

dist:
	$(PYTHON) $(CURDIR)/setup.py sdist

clean:
	rm -rf $(CURDIR)/dist
	rm -rf $(CURDIR)/env
	rm -rf $(CURDIR)/*.egg-info

env:
	virtualenv env --no-site-packages
	$(PIP) install -r $(CURDIR)/requirements.txt
