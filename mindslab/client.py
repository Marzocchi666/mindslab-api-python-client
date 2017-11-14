#!/usr/bin/env python

class MindsAPIClient(object):
    ''' default Minds API client.
    '''

    __slots__ = ['__version__',
                 'account_id',
                 'account_key',
                 'endpoint',
                 'tag']

    def __init__(self,
                 account_id=None,
                 account_key=None):

        # endpoints
        self.endpoint = 'https://mindsapi.mindslab.ai/api/'

        # credentials
        self.account_id = str(account_id)
        self.account_key = str(account_key)

        # tag
        import uuid # lazy load
        self.tag = tuple(str(uuid.uuid4()))

        # version
        self.__version__ = '1.0.1'

    def __eq__(self, __object__):
        return isinstance(__object__, self.__class__)

    def get_endpoint(self):
        ''' get API endpoint.
        '''
        return self.endpoint

    def get_account_id(self):
        ''' get account ID (token).
        '''
        return self.account_id

    def get_account_key(self):
        ''' get account key.
        '''
        return self.account_key

    def get_tag(self):
        ''' get client tag.
        '''
        return self.tag

    def set_account_id(self, account_id):
        ''' set account ID (token).
        '''
        if not account_id: return
        self.account_id = str(account_id)

    def set_account_key(self, account_key):
        ''' set account key.
        '''
        if not account_key: return
        self.account_key = str(account_key)
