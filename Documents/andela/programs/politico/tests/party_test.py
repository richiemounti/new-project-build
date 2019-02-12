import os
import sys
import json
import unittest
from instance.config import configs
from politicer import create_app


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestParty(unittest.TestCase):
    """docstring for TestParty"""

    def setUp(self):
        self.app = create_app(test_config="testing")  
        self.client2= self.app.test_client()

        self.data = {
            "name": "Party A",
            "hqAddress": "50200 Nairobi",
            "logoUrl": "sojri.png"
        }
        self.data1 = {
            "name": "Party B",
            "hqAddress": "50200 Nairobi",
            "logoUrl": "sojri.png"
        }
        self.data2 = {
            "name": "Party C",
            "hqAddress": "50200 Nairobi"
        }
        self.data3 = {
            "name": "co",
            "logoUrl": "sojri.png",
        }
        self.office = {
            "name": "Johny English",
            "type": "Legislative",
        }
        self.office1 = {
            "name": "Johny English",
            "type": "Legislative",
        }
        self.office2 = {
            "name": "Babu Owino",
            "type": "Federal",
        }


    

if __name__ == '__main__':
    unittest.main()
