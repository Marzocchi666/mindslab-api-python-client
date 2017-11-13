#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MindsAPIClient(object):
    ''' Minds API client container.
    '''

    __slots__ = [
        '__version'
        'account_id',
        'account_key',
        'endpoint',
        'tag',
    ]

    def __init__(self,
                 endpoint=None,
                 account_id=None,
                 account_key=None,
                 lang='kr'):

        # endpoints
        self.endpoint = endpoint

        # credentials
        self.account_id = account_id
        self.account_key = account_key

        # tag
        import uuid # lazy load
        self.tag = tuple(str(uuid.uuid4()))

        # version
        self.__version = '1.0.0-beta'

    def get_endpoint(self):
        return self.endpoint

    def get_account_id(self):
        ''' return Account ID.
        '''
        return self.account_id

    def get_account_key(self):
        ''' return Account Key.
        '''
        return self.account_key

    def get_tag(self):
        return self.tag

    def set_account_id(self, account_id):
        ''' set Account ID.
        '''
        if not account_id: return
        self.account_id = str(account_id)

    def set_account_key(self, account_key):
        ''' set Account Key.
        '''
        if not account_key: return
        self.account_key = account_key
