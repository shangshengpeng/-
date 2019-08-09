#!D:\software\Anaconda

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:16:39 2018

@author: dehen
"""

import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip

recent_value = ""
tmp_value=""
while True:
    
    tmp_value = pyperclip.paste()
    
    try:
        if tmp_value != recent_value:
            recent_value = tmp_value          #replace('\n', ' ').replace('\t', ' ').
#            changed = recent_value.replace('\r', ' ').replace('\n', ' ').replace('  ', ' ') #replace("\n", " ")
#            print("\n Value changed: %s" % str(recent_value))
            changed = out = re.sub(r"\s{2,}", " ", recent_value)#re.sub(' +', ' ', recent_value)
            pyperclip.copy(changed)
            print("\n Value changed: %s" % str(changed))
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
    
    
    if tmp_value == 'getend':
#        tmp_value=""
        break