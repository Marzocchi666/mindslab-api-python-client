#!/usr/bin/env python
# -*- coding: utf-8 -*-

from client import MindsAPIClient

try: import requests
except ImportError as error: raise error

import json
import os
import sys

STT_STATUS_OK = 'Success'
STT_STATUS_FAIL = 'Fail'

class MindsSTTClient(MindsAPIClient):
    ''' Minds API STT client.
    '''

    def __init__(self,
                 lang='kr',
                 level=None,
                 sampling='8000'):

        # loads super class
        super(MindsSTTClient, self).__init__()

        # endpoint
        self.endpoint += 'stt/'

        # stt model
        self.lang = lang
        self.level = level
        self.sampling = sampling

        # metadata
        self.__version__ = '0.2.2'

    #
    # public
    #

    def get_config(self):
        '''
        '''
        return dict([
            ('lang', self.lang),
            ('level', self.level),
            ('sampling', self.sampling)
        ])

    def set_config(self,
                   lang,
                   level,
                   sampling):
        '''
        '''
        self.lang = lang
        self.level = level
        self.sampling = sampling

    def get_models(self, verbose=False):
        ''' retrieve available STT models from server.
        '''
        data = {
            'cmd': 'getSTTModels',
            'ID': self.account_id,
            'key': self.account_key
        }
        with requests.post(
                self.endpoint,
                files={},
                data=data
        ) as res:
            if res.status_code != 200: return
            try:
                payload = json.loads(res.text)
                status = payload.get('status')
            except: return
            if status == STT_STATUS_OK:
                stt_models = json.loads(payload.get('data'))
            else:
                stt_models = payloads.get('data')
            if verbose: sys.stdout.write('%s\n' % stt_models)
            return (stt_models, status)

    def transcribe_audio_file(self, files=[], verbose=False):
        '''
        '''
        data = {
            'cmd': 'runFileStt',
            'ID': self.account_id,
            'key': self.account_key,
            'lang': self.lang,
            'sampling': self.sampling,
            'level': self.level
        }
        if isinstance(files, basestring):
            return [ self.__get_transcription(audio_file=files,
                                              data=data,
                                              verbose=verbose) ]
        elif isinstance(files, list) or isinstance(files, tuple):
            return [ self.__get_transcription(audio_file=file,
                                              data=data,
                                              verbose=verbose)
                     for file in files ]
        else: return []

    #
    # private
    #

    def __get_transcription(self, audio_file, data={}, verbose=False):
        '''
        '''
        if not (os.path.exists(audio_file) or os.path.isfile(audio_file)):
            sys.stderr.write("[-] '%s' does not exist.\n" % audio_file)
            return
        with open(audio_file, 'rb') as f:
            audio_stream = {'file': f}
        with requests.post(self.endpoint, files=audio_stream, data=data) as res:
            if res.status_code != 200: return
            try:
                payload = json.loads(res.text)
                status = payload.get('status')
                data = payload.get('data')
            except: return
        if verbose: sys.stdout.write('%s:%s\n' % (status, data))
        return (status, data)
