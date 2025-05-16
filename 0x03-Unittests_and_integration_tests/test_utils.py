#!/usr/bin/env python3
"""testing utils.py"""

import unittest
from typing import Dict, Mapping, Tuple, Union
from unittest.mock import MagicMock, patch

from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """test that the access_nested_map function works"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Tuple[str],
                               expected: Union[int, Dict]) -> None:
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Tuple[str],
                                         exc: Exception) -> None:
        """Uses the assertRaises context manager to test
        that a KeyError is raised when needed"""
        with self.assertRaises(exc):
            """can also be: self.assertRaises(KeyError,
            access_nested_map, nested_map, path)"""
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self,
                      url: str,
                      payload: Dict, mock_get: MagicMock) -> None:
        """mock get request"""
        # mock_get is the mock obj created by patch
        mock_get.return_value = payload
        mock_resp = mock_get(url)

        # check that mock response equals payload checked atm
        self.assertEqual(mock_resp, payload)
        mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """memoize tests"""

    def test_memoize(self):
        """test memoize"""

        class TestClass:
            """a test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        @patch.object(TestClass, 'a_method')
        def test(mock_method: MagicMock):
            """test that a_method is called once.
            here patch has created the mock object
            so assign value only
            """
            mock_method.return_value = 42
            tstcls = TestClass()
            tstcls.a_property
            tstcls.a_property
            mock_method.assert_called_once()

        test()
