#!/usr/bin/python3
import inspect
import unittest
import pycodestyle


class TestClassDocumentation():

    def __init__(self, , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tests = tests
        self.name = _class

        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def documentation(self):
        with self.test.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):

                    doc = f[1].__doc__
                    self.tests.asssertGreaterEqual(
                        len(doc), 1,
                        'Method {} lacks documentation'.format(f[0]))

        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.test.assertGreaterEqual(len(doc), 1,
                                         'Class lacks documentation')

    def pep8(self, files):

        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnigs).')


if __name__ == '__main__':
    unittest.main()
