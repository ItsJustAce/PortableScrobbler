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

version = "0.4.3"
    
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

#basedir.xdg_config_dirs.insert(0, "./configs")  # for debugging only

def _get_config_path(*resources):
    """
        Returns a path to a configs file
        according to the xdg standards.
    """
    
    if "XDG_CONFIG_HOME" in os.environ:
        base = os.path.join(os.environ["XDG_CONFIG_HOME"], "scrobblethis")
    else:
        base = os.path.expanduser("~/.config/scrobblethis")
    
    path = base
    for resource in resources:
        path = os.path.join(path, resource)
    
    return path
