
import unittest
import json
from .party_test import TestParty 

class PartyTests(TestParty):
    '''Party tests are done here '''

    def test_posting_a_party(self):
        res = self.client2.post(path='/v1/admin/party', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(res.status_code, 201) 
    
    def test_getting_all_parties(self):
        res = self.client2.get(path='/v1/user/party', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_getting_a_single_party(self):
        post = self.client2.post(path='/v1/admin/party', data=json.dumps(self.data1), content_type='application/json')
        res = self.client2.get(path='v1/user/party/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_editing_a_party(self):
        post = self.client2.post(path='/v1/admin/party', data=json.dumps(self.data1), content_type='application/json')
        res = self.client2.patch(path='v1/admin/party/1', data=json.dumps(self.data2), content_type='application/json')
        self.assertEqual(res.status_code, 202)


    def test_deleting_a_party(self):
        post = self.client2.post(path='/v1/admin/party', data=json.dumps(self.data1), content_type='application/json')
        res = self.client2.delete(path='v1/admin/party/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)



    if __name__ == '__main__':
        unittest.main()
