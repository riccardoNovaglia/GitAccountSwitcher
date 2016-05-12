from unittest import TestCase

import os


class TestWriteToFile(TestCase):
    def test_throws_exception_if_unknown_path(self):
        try:
            with open('some/path', 'w+') as f:
                f.write('something')
            self.fail('Should have thrown and exception')
        except Exception as e:
            self.assertIsInstance(e, IOError)
            self.assertEqual('No such file or directory', e.strerror)

    def test_can_check_if_path_exists(self):
        duh_exists = os.path.exists('/')

        self.assertTrue(duh_exists)

        doesnt_exist = os.path.exists('some/path')

        self.assertFalse(doesnt_exist)

    def test_can_check_before_throwing(self):
        path = 'some/path'
        if os.path.exists(path):
            with open(path, 'w+') as f:
                f.write('something')
            self.fail('This should not have existed..')
