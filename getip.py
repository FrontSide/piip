#!/usr/bin/env python3

import re
import netifaces

IGNORE_IPS_REGEX=[re.compile(ipre) for ipre in ['127.*']]

def _is_valid_ip(ip):
    for ignore_ipre in IGNORE_IPS_REGEX:
        if ignore_ipre.match(ip):
            return False
    return True


def get_ips():
    
    ips = []
    for ifcname in netifaces.interfaces():
    
        ifc = netifaces.ifaddresses(ifcname)
        if ifc.get(netifaces.AF_INET):
            ips.append(ifc[netifaces.AF_INET][0]['addr'])
        
    return [ip for ip in ips if _is_valid_ip(ip)]

