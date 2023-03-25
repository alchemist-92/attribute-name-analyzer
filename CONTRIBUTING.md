# attribute-name-analyzer

[Development Environment Setup](https://link-to-dev-setup.git)

## Install

```shell script
git clone https://github.com/alchemist-92/attribute-name-analyzer.git
cd attribute-name-analyzer
make
```

## Create a Feature Branch

This project adheres to a feature branching strategy with the following naming
conventions:

| Issue Type | Branch Name Pattern    |
|:-----------|:-----------------------|
| Feature    | feature/{ISSUE_DESC}   |
| Bug        | bugfix/{ISSUE_DESC}    |

## Testing

Please create a unit test for any/all public functions or methods you
introduce.

To *run* unit tests for this package, just run `make test` in the project
directory.

## [Create a Pull Request](https://github.com/alchemist-92/attribute-name-analyzer/pulls)

## Upgrade/Update Requirements

If/when you upgrade or add dependencies to setup.cfg, you will need to
run `make requirements` before committing (and before testing, even locally,
with tox).

To update *existing requirements* to reflect the most recent compatible
versions, run `make upgrade` (this will also update requirements once upgrades are complete).

Run `make reinstall`, to circumvent pinned requirements from the requirements.txt file,
suitable for use when requirements.txt has versions with conflicting dependencies.


## Deployment

Distribution of this package to Artifactory will occur when your changes are
merged into the "master" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

Distribution of this package to Artifactory will occur when your changes are
merged into the "master" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.
