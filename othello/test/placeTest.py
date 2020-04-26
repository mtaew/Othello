'''
    Created on Apr 26, 2020
    
    @author:    Tae Myles
'''
from unittest import TestCase
from othello.place import _place as place


class Test(TestCase):
    def setUp(self):
        self.parms = {'op': 'place', 'light': '1', 'dark': '2', 'blank': '0', 'location': '1:1',
                      'board': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
                      }


    def tearDown(self):
        self.parms = {'op': 'place', 'light': '1', 'dark': '2', 'blank': '0', 'location': '1:1',
                      'board': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
                      }


    def test900_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '10'
        expected = 'error: above bound light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test901_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '-1'
        expected = 'error: below bound light value'
        self.actual = place(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()