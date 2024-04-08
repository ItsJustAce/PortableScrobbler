from distutils.core import setup

setup(name = "portablescrobbler",
version = "0.1.1",
description = "Command-line portable player log scrobbler",
author = "Tom (ItsJustAce) <justace0@protonmail.me>",
author_email = "justace0@protonmail.me",
license = "gpl",
url = "https://github.com/ItsJustAce/PortableScrobbler",
scripts = ["portablescrobbler"],
packages = ["st"],
data_files = [
    ("/usr/share/man/man1", ("scrobblethis.1.gz",)),
    ]
install_requires=["pylast"]
)

