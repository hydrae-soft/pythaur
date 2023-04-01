from git import Repo
from os import chdir, system
from os.path import isdir
from typing import List

from models.package import Package


def clone(pkgs: List[Package]):
    i = 0
    while i < len(pkgs):
        p = pkgs[i]
        if not isdir(p.directory):
            print('Cloning %s.' % p.git_url)
            Repo.clone_from(p.git_url, p.directory)
        else:
            print('\"%s\" package already exists.' % p.name)
        i += 1


def install(packages: List[Package]):
    for p in packages:
        chdir(p.directory)
        system('makepkg -s')
        system('sudo pacman -U --needed --noconfirm *.zst')
