#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dir):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dir))


if __name__ == '__main__':

    if not "{{ cookiecutter.approvaltests_geo_data_root }}":
        remove_file('pytest.ini')

    if "{{ cookiecutter.vsc_repo }}" == 'gitlab':
        remove_dir(".github")
    elif "{{ cookiecutter.vsc_repo }}" == 'github':
        remove_file(".gitlab-ci.yml")
    else:
        raise NotImplementedError(
            "The repository {{ cookiecutter.vsc_repo }} specified in cookiecutter.vsc_repo, is currently not supported.\nSpecify either 'gitlab' or 'github'")
