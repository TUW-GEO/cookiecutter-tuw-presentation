.ONESHELL:
SHELL = /bin/bash

BASENAME = {{cookiecutter.project_slug}}
CONDA_ENV_DIR = $(shell conda info --base)/envs/{{cookiecutter.project_slug}}
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

all: revealjs beamer pptx

revealjs: environment
	quarto render

beamer: $(BASENAME).qmd environment
	quarto render $^ --metadata-file _authors.yml --to beamer

pptx: $(BASENAME).qmd environment
	quarto add --no-prompt kapsner/authors-block
	quarto render $^ --metadata-file _authors.yml --to pptx

help:
	@echo "make clean"
	@echo " clean all python build/compilation files and directories"
	@echo "make environment"
	@echo " create the base environment for the project"
	@echo "make install"
	@echo " install dependencies in active environment"
	@echo "make test"
	@echo " install dependencies for tests in active python environment if necessary and run test with coverage"
	@echo "make version"
	@echo " update _version.py with current version tag"
	@echo "make dist"
	@echo " build the package ready for distribution and update the version tag"

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +
	rm --force .coverage
	rm --force --recursive .pytest_cache
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
	rm --force .install.done
	rm --force .install.test.done

$(CONDA_ENV_DIR):
	@echo "creating new base {{cookiecutter.project_slug}} conda environment..."
	conda create -y -c conda-forge -n {{cookiecutter.project_slug}} python=3.9 pip mamba jupyter
	$(CONDA_ACTIVATE) {{cookiecutter.project_slug}}
	mamba install -y -c conda-forge matplotlib numpy
	@echo "... finished."

environment: $(CONDA_ENV_DIR)
	@echo -e "conda environment is ready. To activate use:\n\tconda activate {{cookiecutter.project_slug}}"

.PHONY: help clean environment 