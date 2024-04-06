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

import collections, codecs, time, glob, os, json
import st.common

class UnsupportedProtocolError(Exception):
    def __str__(self):
        return "Unsupported protocol version"

Track = collections.namedtuple("Track", 
    ["artist", "album", "title", "position", "duration", "rating", "timestamp", "musicbrainz"])

def get_tz_offset():
    """
    Returns the timezone offset in plus or minus seconds.
    Ex: If UTC+2, it would be 12*60==7200 secs
    """
    
    if time.localtime().tm_isdst:
        return -1*time.altzone
    else:
        return -1*time.timezone
        
def parse(path):
    """ Parses the log and returns a sequence of Track """
    
    # read the text
    lines = codecs.open(path, "r", "utf-8").read().strip().split('\n')
    
    # check protocol
    if lines[0] != "#AUDIOSCROBBLER/1.1":
        raise UnsupportedProtocolError()
    
    # check if UTC timestamps or local
    if lines[1] == "#TZ/UTC":
        tz_offset = 0
    else:
        tz_offset = get_tz_offset()
    
    # read tracks
    tracks = []
    for line in lines[3:]:
        v = line.split('\t')
        if len(v) < 8:
            v = v + [""]*(8-len(v)) # pad v with empty strings
        v[6] = str(int(v[6]) - tz_offset)
        track = Track(*v)
        if track.rating == "L":
            tracks.append(track)
    
    return tracks

def _get_history():
    try:
        fp = open(st.common._get_config_path("history"))
        return json.load(fp)
    except IOError:
        return []
    
def _add_to_history(*paths):
    json.dump(list(set(paths)), open(common._get_config_path("history"), "w"))

def get_paths(*paths):
    """
    Returns paths to ".scrobbler.log" files. 
    The input paths are specified by the user. If the user
    did not specify any, We check the history and probe around
    for logs.
    """
    
    if not paths:
        # load history and proble around for a log
        paths = _get_history() + glob.glob("/media/*") + glob.glob("/mnt/*")
    else:
        # just use it and and it to history for later
        _add_to_history(*paths)
    
    l = []
    for path in paths:
        path = os.path.expanduser(path)
        
        if not path.endswith(".scrobbler.log"):
            path = os.path.join(path, ".scrobbler.log")
            
        if os.path.exists(path):
            l.append(path)
    
    return l
