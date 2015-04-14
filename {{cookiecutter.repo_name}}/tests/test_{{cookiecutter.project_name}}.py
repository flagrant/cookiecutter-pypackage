#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_name }}
----------------------------------

Tests for `{{ cookiecutter.project_name }}` module.
"""

import unittest

from {{ cookiecutter.project_name }} import {{ cookiecutter.project_name }}


class Test{{ cookiecutter.project_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
