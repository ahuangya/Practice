# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_unittest.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************
import unittest


class FalseTest(unittest.TestCase):

    def testTruth(self):
        self.assertTrue(True)

    def testFalse(self):
        self.assertFalse(False)


class EequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(2, 2)

    def testNotEqual(self):
        self.assertNotEqual(1, 2)


class FixturesTest(unittest.TestCase):

        def setUp(self):
            self.fixture = range(1, 10)

        def tearDown(self):
            del self.fixture

        def test(self):
            self.assertEqual(self.fixture, range(1, 10))


def raise_error(*args, **kwds):
    raise ValueError('Invalid value:%s%s' % (args, kwds))


class ExcetpionTest(unittest.TestCase):

    def test_locally(self):
        try:
            raise_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_raise(self):
        self.assertRaises(ValueError, raise_error, 'a', b='c')

if __name__ == '__main__':
    unittest.mian()
