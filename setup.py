from distutils.core import setup

import os

def get_build():
    path = "./.build"
    
    if os.path.exists(path):
        fp = open(path, "r")
        build = eval(fp.read())
        if os.path.exists("./.increase_build"):
            build += 1
        fp.close()
    else:
        build = 1
    
    fp = open(path, "w")
    fp.write(str(build))
    fp.close()
    
    return int(build)

setup(
    name = "portablescrobbler",
    version = "0.1.%d" %get_build(),
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
    )
    
