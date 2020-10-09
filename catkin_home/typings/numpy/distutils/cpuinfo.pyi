"""
This type stub file was generated by pyright.
"""

import sys
import platform

"""
cpuinfo

Copyright 2002 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@cens.ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy (BSD style) license.  See LICENSE.txt that came with
this distribution for specifics.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
Pearu Peterson

"""
if sys.version_info[0] >= 3:
    ...
else:
    ...
def getoutput(cmd, successful_status=..., stacklevel=...):
    ...

def command_info(successful_status=..., stacklevel=..., **kw):
    ...

def command_by_line(cmd, successful_status=..., stacklevel=...):
    ...

def key_value_from_command(cmd, sep, successful_status=..., stacklevel=...):
    ...

class CPUInfoBase(object):
    """Holds CPU information and provides methods for requiring
    the availability of various CPU features.
    """
    def __getattr__(self, name):
        ...
    


class LinuxCPUInfo(CPUInfoBase):
    info = ...
    def __init__(self) -> None:
        ...
    
    _is_i386 = ...
    _is_Xeon = ...


class IRIXCPUInfo(CPUInfoBase):
    info = ...
    def __init__(self) -> None:
        ...
    
    def get_ip(self):
        ...
    


class DarwinCPUInfo(CPUInfoBase):
    info = ...
    def __init__(self) -> None:
        ...
    


class SunOSCPUInfo(CPUInfoBase):
    info = ...
    def __init__(self) -> None:
        ...
    


class Win32CPUInfo(CPUInfoBase):
    info = ...
    pkey = ...
    def __init__(self) -> None:
        ...
    


if sys.platform.startswith('linux'):
    cpuinfo = LinuxCPUInfo
else:
    cpuinfo = IRIXCPUInfo
cpu = cpuinfo()
