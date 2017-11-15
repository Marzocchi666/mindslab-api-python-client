#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .client import MindsAPIClient

try: import requests
except ImportError as error: raise error

import json
import os
import sys

NLA_STATUS_OK = 'Success'
NLA_STATUS_FAIL = 'Fail'

class MindsNLAClient(MindsAPIClient):
    ''' Minds API NLA client.
    '''

    def __init__(self,
                 lang='kr',
                 level=None,
                 keyword='8000'):

        # loads super class
        super(MindsNLAClient, self).__init__()

        # endpoint
        self.endpoint += 'nla/'

        # nla model
        self.level = level
        self.keyword_level = keyword

        # metadata
        self.__version__ = '0.1.0'

    #
    # public
    #

    def get_model(self):
        '''
        '''
        return dict([
            ('level', self.level),
            ('keyword_level', self.keyword_level)
        ])

    def set_model(self,
                   level,
                   keyword_level):
        '''
        '''
        self.level = level
        self.keyword_level = keyword_level

    def get_nla_result(self,
                       sentence,
                       verbose=False):
        '''
        '''
        data = {
            'cmd': 'runNLA',
            'ID': self.account_id,
            'key': self.account_key,
            'level': self.level,
            'keyword_level': self.keyword_level,
            'sentence': str(sentence)
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
