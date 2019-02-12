import unittest
import json
from .party_test import TestParty 

class OfficeTests(TestParty):
    '''Office tests are done here '''

    def test_posting_an_office(self):
        res = self.client2.post(path='/v1/admin/office', data=json.dumps(self.office), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_getting_all_offices(self):
        res = self.client2.get(path='/v1/user/office', content_type='application/json')
        self.assertEqual(res.status_code, 200)
    
    def test_getting_a_single_party(self):
        post = self.client2.post(path='/v1/admin/office', data=json.dumps(self.office1), content_type='application/json')
        res = self.client2.get(path='v1/user/office/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_editing_a_party(self):
        post = self.client2.post(path='/v1/admin/office', data=json.dumps(self.office), content_type='application/json')
        res = self.client2.patch(path='v1/admin/office/1', data=json.dumps(self.office2), content_type='application/json')
        self.assertEqual(res.status_code, 202)

