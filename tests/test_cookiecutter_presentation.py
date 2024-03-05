import subprocess
import os
import webbrowser

def test_bake_project(cookies):
    result = cookies.bake(extra_context={  
        "author": "TU Wien GEO MRS group",
        "author_email": "remote.sensing@geo.tuwien.ac.at",
        "project_name": "my-tuw-project",
        "project_description": "my project description",
        "url": ""})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my_tuw_project"
    assert result.project_path.is_dir()

    os.chdir(result.project_path)

    assert subprocess.run(['make', 'revealjs']).returncode == 0
    webbrowser.open_new_tab(os.path.join(result.project_path, 'public/index.html'))
    assert subprocess.run(['conda', 'remove', '-n', 'my_tuw_project', '--all', '-y']).returncode == 0