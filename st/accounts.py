# 
# Copyright 2009 Amr Hassan <amr.hassan@gmail.com>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import pylast, hashlib, os
import st.common

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

class Account(object):
    def __init__(self, name, type, username, password, password_hash, submit_url, client_version):
    
        self.name = name
        self.username = username
        self.type = type
        
        if not password_hash:
            password_hash = hashlib.md5(password).hexdigest()
        
        if type == "lastfm":
            self.network = pylast.get_lastfm_network(username = username, password_hash = password_hash)
        elif type == "librefm":
            self.network = pylast.get_librefm_network(username = username, password_hash = password_hash)
        elif type == "custom":
            self.network = pylast.get_lastfm_network(username = username, password_hash = password_hash)
            self.network.submission_server = submit_url
        
        self.scrobbler = self.network.get_scrobbler("sth", client_version)
        self.cache = []
    
    def add_to_scrbble_cache(self, track):
        self.cache.append([track.artist, track.title, track.timestamp, pylast.SCROBBLE_SOURCE_USER,
                                pylast.SCROBBLE_MODE_PLAYED, track.duration, track.album, track.position,
                                track.musicbrainz])
                                
    def scrobble(self):
        self.scrobbler.scrobble_many(self.cache)
    
    def __repr__(self):
        return self.name

def get_accounts():    
    c = configparser.ConfigParser(defaults={"password": "", "md5_password_hash": "", "submit_url": ""})
    
    accounts_config_path = st.common._get_config_path("accounts.config")
    
    l = []
    if os.path.exists(accounts_config_path):
        c.read(accounts_config_path)
        
        for name in c.sections():
            l.append(Account(name = name,
                                    type = c.get(name, "type"),
                                    username = c.get(name, "username"),
                                    password = c.get(name, "password"),
                                    password_hash = c.get(name, "md5_password_hash"),
                                    submit_url = c.get(name, "submit_url"),
                                    client_version = st.common.version
                                    ))
        
    return l

def write_default_accounts():
    text = """# Enable one or more of these accounts
# 
# You can either provide your passwords or your md5 hash. To get a md5 of a string type this into a shell:
# python -c "import getpass, hashlib; print(hashlib.md5(getpass.getpass().encode('utf-8')).hexdigest())"
# 
#
#A sample Last.fm account. Uncomment this section to use it.
#[MyLastfmAccount]
#type = lastfm
#username = 
#password = 
#md5_password_hash = 
#
#A sample Libre.fm account. Uncomment this section to use it.
#[MyLibrefmAccount]
#type = librefm
#username = 
#password = 
#md5_password_hash = 
#
#A sample custom account account
#[MyCustomAccount]
#type = custom
#submit_url = 
#username = 
#password = 
#md5_password_hash = """
    
    
    path = st.common._get_config_path("accounts.config")
    
    if os.path.exists(path): return
    
    def make_dir(path):
        first_level = os.path.dirname(path)
        if not os.path.exists(os.path.dirname(first_level)):
            make_dir(os.path.dirname(first_level))
        
        os.mkdir(first_level)
    
    make_dir(path)
    
    fp = open(path, "w")
    fp.write(text)
    fp.close()
