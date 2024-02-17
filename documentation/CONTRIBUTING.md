# attribute-name-validator

[Development Environment Setup](https://github.com/siddartham/dev-env-setup/blob/main/python-enterprise-auth-dev-setup.md)

## Install

```shell script
git clone "https://github.com/siddartham/attribute-name-validator.git"
cd attribute-name-validator
make
```
## Contribution

To add a new **enterprise approved class word** or **acronym** to the tool.
1. create a feature branch as stated below.
2. To add a new entry(acronym or class word) to the tool for analysis
   1. Add it in the respective sheet
   2. Run `make update-catalog` - this updates the metadata used by the package
3. To update schema of the objects to extend the reports or input file schema
   1. Run `make remodel` to update `scripts/remodel.py` with the needed schema
   2. Run `make update-catalog` to parse with the updated schema
4. Run `pytest` to generate analysis reports on test data with updated schema
5. Run `make upgrade` to update the dependencies.
6. Fix any type hinting issues highlighted after running `mypy`
7. Run `black .` to auto edit code to follow PEP8 recommendations
8. Run `flake8`
9. Run `tox` for CI testing of all 3 - pytest, mypy, black
10. Upgrade minor version in setup.py
11. Post PR for review

## Create a Feature Branch


## Testing

Please create a unit test for any/all public functions or methods you
introduce.

To *run* unit tests for this package, just run `make test` in the project
directory.

## [Create a Pull Request](https://github.com/siddartham/attribute-name-validator/pulls)

## Upgrade/Update Requirements

If/when you upgrade or add dependencies to setup.cfg, you will need to
run `make requirements` before committing (and before testing, even locally,
with tox).

To update *existing requirements* to reflect the most recent compatible
versions, run `make upgrade` (this will also update requirements once
upgrades are complete).

## Deployment

Distribution of this package to Artifactory will occur when your changes are
merged into the "master" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

Distribution of this package to Artifactory will occur when your changes are
merged into the "master" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.
