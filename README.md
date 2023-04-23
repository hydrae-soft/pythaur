# pythaur
A Python based AUR (Arch User Repository) helper.

## Usage

pythaur [-h] -i INSTALL [INSTALL ...] [-c]

options:
  -h, --help            show this help message and exit
  -i INSTALL [INSTALL ...], --install INSTALL [INSTALL ...]
                        Use this flag to specify the names of the packages to
                        be installed.
  -c, --cleanup         Removes cloned files.

**Example:** pythaur -c -i package