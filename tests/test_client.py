#!/usr/bin/env python

from src.client import MindsAPIClient

import unittest

class TestMindsAPIClient(unittest.TestCase):
    ''' unit test for Minds API client container.
    '''

    def test_client_initialization(self):
        client = MindsAPIClient()
        self.assertTrue(client != None)
        self.assertTrue(isinstance(client, MindsAPIClient))
