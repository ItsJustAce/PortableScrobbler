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
    name = "scrobblethis",
    version = "0.4.%d" %get_build(),
    description = "Command-line portable player log scrobbler",
    author = "Amr Hassan <amr.hassan@gmail.com>",
    author_email = "amr.hassan@gmail.com",
    license = "gpl",
    url = "https://launchpad.net/scrobblethis",
    scripts = ["scrobblethis"],
    packages = ["st"],
    data_files = [
        ("/usr/share/man/man1", ("scrobblethis.1.gz",)),
        ]
    )
    
