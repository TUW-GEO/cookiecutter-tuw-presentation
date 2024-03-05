.ONESHELL:
SHELL = /bin/bash

BASENAME = {{cookiecutter.project_slug}}
CONDA_ENV_DIR = $(shell conda info --base)/envs/{{cookiecutter.project_slug}}
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

all: beamer pptx revealjs

revealjs: $(BASENAME).qmd environment
	$(CONDA_ACTIVATE) {{cookiecutter.project_slug}}
	quarto render $^ --output-dir public

beamer: $(BASENAME).qmd environment
	$(CONDA_ACTIVATE) {{cookiecutter.project_slug}}
	quarto add --no-prompt kapsner/authors-block
	quarto render $^ --metadata-file _authors.yml --to beamer

pptx: $(BASENAME).qmd environment
	$(CONDA_ACTIVATE) {{cookiecutter.project_slug}}
	quarto add --no-prompt kapsner/authors-block
	quarto render $^ --metadata-file _authors.yml --to pptx

help:
	@echo "make revealjs"
	@echo " Render revealjs presentation"
	@echo "make environment"
	@echo " create the base environment for the project"

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
	mamba install -y -c conda-forge matplotlib numpy xarray pandas dask
	@echo "... finished."

environment: $(CONDA_ENV_DIR)
	@echo -e "conda environment is ready. To activate use:\n\tconda activate {{cookiecutter.project_slug}}"

.PHONY: help clean environment 