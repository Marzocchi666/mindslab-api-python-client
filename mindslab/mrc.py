#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .client import MindsAPIClient

try: import requests
except ImportError as error: raise error

import json
import os
import sys

MRC_STATUS_OK = 'Success'
MRC_STATUS_FAIL = 'Fail'

class MindsMRCClient(MindsAPIClient):
    ''' Minds API MRC client.
    '''

    def __init__(self):

        # loads super class
        super(MindsMRCClient, self).__init__()

        # endpoint
        self.endpoint += 'mrc/'

        # metadata
        self.__version__ = '0.1.0'

    #
    # public
    #

    def get_mrc_result(self,
                       question,
                       sentence,
                       verbose=False):
        '''
        '''
        data = {
            'cmd': 'runMRC',
            'ID': self.account_id,
            'key': self.account_key,
            'question': question,
            'sentence': sentence
        }
        with requests.post(self.endpoint, data=data) as res:
            if res.status_code != 200: return
            try:
                payload = json.loads(res.text)
                status = payload.get('status')
                data = payload.get('data')
            except: return
        if verbose: sys.stdout.write('%s:%s\n' % (status, data))
        return (status, data)
