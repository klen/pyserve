PYTHON=$(CURDIR)/env/bin/python
PIP=$(CURDIR)/env/bin/pip

.PHONY: all clean update serve register upload

all: env dist update

dist:
	$(PYTHON) $(CURDIR)/setup.py sdist

clean:
	rm -rf $(CURDIR)/dist
	rm -rf $(CURDIR)/env
	rm -rf $(CURDIR)/*.egg-info
	find $(CURDIR) -name "*.pyc" -delete

env:
	virtualenv env --no-site-packages
	$(PIP) install -r $(CURDIR)/requirements.txt

update:
	$(PYTHON) setup.py develop

serve:
	$(CURDIR)/env/bin/serve

register:
	$(PYTHON) setup.py register

upload: dist register
	$(PYTHON) $(CURDIR)/setup.py upload
