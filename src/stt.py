#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .client import MindsAPIClient

import requests
import json
import os

class MindsSTTClient(MindsAPIClient):
    ''' Minds API STT client.
    '''

    def __init__(self,
                 lang='kr',
                 level=None,
                 sampling='8000'):

        # load MindsAPIClient
        super(MindsAPIClient, self).__init__()

        # stt model
        self.lang = lang
        self.level = level
        self.sampling = sampling

        # metadata
        self.__version = '0.2.1'

    def __version__(self):
        return self.__version

    def get_model(self):
        '''
        '''
        return dict([
            ('lang', self.lang),
            ('level', self.level),
            ('sampling', self.sampling)
        ])

    def set_model(self,
                  lang,
                  level,
                  sampling):
        '''
        '''
        self.lang = lang
        self.level = level
        self.sampling = sampling
