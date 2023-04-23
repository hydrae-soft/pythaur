from os import chdir, mkdir
from os.path import isdir
import subprocess

# Where path is the destination of the cloned files.
def clone(pkgs: list, path: str):
    if not isdir(path):
        mkdir(path)
    for p in pkgs:
        if not isdir(p.directory):
            subprocess.run(['git', 'clone', p.git_url], cwd=path)


def install(pkgs: list):
    for p in pkgs:
        subprocess.run(['makepkg', '-s', '-i'], cwd=p.directory)

