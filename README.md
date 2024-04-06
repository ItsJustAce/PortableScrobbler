# PortableScrobbler
A CLI log scrobbler for your portable devices.

Based on [this](https://code.launchpad.net/scrobblethis) orphaned package last updated in 2011.
WARNING: Log files will be deleted once uploaded to prevent double scrobbling.

# Requirements
- Python

# Usage
Upload log:

```sh
portablescrobbler "/path/to/.scrobbler.log"
```

Once the path is specified, you will be asked to authenticate via browser with the API. If you have already specified a path previously it should be remembered. 
