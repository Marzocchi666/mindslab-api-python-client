#!/usr/bin/env python

import mindslab-api-python-client

from mindslab-api-python-client import client
from mindslab-api-python-client import mrc
from mindslab-api-python-client import nla
from mindslab-api-python-client import stt

_SUBMODULES = {
    'client': client,
    'mrc': mrc,
    'nla': nla,
    'stt': stt
}

# create module aliases to mindslab.*
import sys
for module_name, module in iteritems(_SUBMODULES):
    sys.modules['mindslab.%s' % module_name] = module
