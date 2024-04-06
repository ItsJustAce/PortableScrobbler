# PortableScrobbler
A CLI log scrobbler for your portable devices.

Based on [this](https://code.launchpad.net/scrobblethis) orphaned package last updated in 2011. It utilised config files stating passwords in plain texts. This package rewrites the code to use last.fm's API to authenticate and connect your account for scrobbling.

WARNING: Log files will be deleted once uploaded to prevent double scrobbling.

# Requirements
- Working on Python 3.11.8
- PyLast

# Usage
Upload log:

```sh
portablescrobbler "/path/to/.scrobbler.log"
```

Once the path is specified, you will be asked to authenticate via browser with the API. If you have already specified a path previously it should be remembered. 
