#!/usr/bin/env python

from mindslab.client import MindsAPIClient
from mindslab.nla import MindsNLAClient

import unittest
import sys

class TestMindsNLAClient(unittest.TestCase):
    ''' unit test for Minds NLA client.
    '''

    client = MindsAPIClient()
    nla = MindsNLAClient()

    def test_client_initialization(self):
        self.assertFalse(self.nla.__eq__(None))
        self.assertTrue(isinstance(self.nla, MindsAPIClient))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMindsNLAClient)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(test_suite))
    sys.exit(not result.wasSuccessful())
