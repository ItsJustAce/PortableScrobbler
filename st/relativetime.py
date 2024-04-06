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

import time

def _plural(quantity, singular, plural=None):
    if plural == None:
        plural = singular + "s"
    
    if int(quantity) == 1:
        return singular
    else:
        return plural
    

def get_relative_time(timestamp):
    
    diff = time.time() - int(timestamp)
    
    if diff < 60:
        return "Less than a minute ago"
    elif diff < 60*60:
        return "%d %s ago" %(diff/60, _plural(diff/60, "minute"))
    elif diff < 24*60*60:
        return "%d %s ago" %(diff/(60*60), _plural(diff/(60*60), "hour"))
    else:
        return time.strftime("%b %d %I:%M %p", time.localtime(float(timestamp)))
