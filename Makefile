SHELL := bash
PYTHON_VERSION := 3.8

dev-install:
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt && \
	pip3 install -r ci_requirements.txt && \
	pip3 install -r requirements.txt -e . && \
	echo "Success!"


ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ venv/Scripts/activate.bat || . venv/bin/activate ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r requirements.txt && \
	echo "Installation complete"

install:
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -c requirements.txt -e . && \
	echo "Success!"

# This will circumvent pinned requirements from the requirements.txt file,
# and is suitable for use when requirements.txt has versions with
# conflicting dependencies.
reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt -r ci_requirements.txt -e . && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements freeze\
	 -nv '*' . pyproject.toml tox.ini ci_requirements.txt\
	 > .requirements.txt && \
	pip3 install --upgrade --upgrade-strategy eager\
	 -r .requirements.txt -e . && \
	rm .requirements.txt && \
	make requirements && \
	echo "Upgrade completed successfully!"

clean:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools uninstall-all\
	 -e dev_requirements.txt\
	 -e ci_requirements.txt\
     -e pyproject.toml\
     -e tox.ini\
	 -e . && \
	daves-dev-tools clean && \
	echo "Cleanup completed successfully!"

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements update -nv flake8 && \
	echo "Requirements updated successfully!"

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	if [[ "$$(python -V)" = "Python 3.8."* ]] ;\
	then tox -r -p ;\
	else tox -r -e pytest ;\
	fi

format:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	black . && isort . && flake8



remodel:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 scripts/remodel.py
	black .

update-catalog:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 scripts/update_catalog.py

clear-parsed-data:
	rm attribute_name_validator/*.json
	rm attribute_name_validator/*.html
	rm attribute_name_validator/*.xlsx
	rm -rf reports

.PHONY: reports
reports:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	make clear-parsed-data -i
	pytest
