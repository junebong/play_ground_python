# -*- coding:utf-8 -*-

import unittest

class HelloWorldTest(unittest.TestCase):
    
    def printTest(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("IN")
    
    def printTest2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
    print("IN")