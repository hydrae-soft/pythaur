from urllib.error import HTTPError
from urllib.request import urlopen

class Package:

    def __init__(self, name: str, directory: str):
        aur_url = 'https://aur.archlinux.org/'
        self.__name = name
        self.__details_url = aur_url + 'packages/' + name
        self.__git_url = aur_url + name + '.git'
        self.__directory = directory

    @property
    def name(self) -> str:
        return self.__name

    @property
    def details_url(self) -> str:
        return self.__details_url

    @property
    def git_url(self) -> str:
        return self.__git_url

    @property
    def directory(self) -> str:
        return self.__directory

def is_on_aur(package: Package) -> bool:
    try:
        if urlopen(package.details_url).getcode() == 200:
            return True
    except HTTPError:
        print('\"%s\" package was not found in AUR. HTTPError.\n' % package.name)
    return False

