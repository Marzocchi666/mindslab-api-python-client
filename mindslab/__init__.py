#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Alias for MindsLab API client.
'''

import mindslab-api-python-client

from mindslab-api-python-client import client
from mindslab-api-python-client import stt

_SUBMODULES = {
    'client': client,
    'stt': stt
}

# create aliases to mindslab.*
import sys
for module_name, module in iteritems(_SUBMODULES):
    sys.modules['mindslab.%s' % module_name] = module
