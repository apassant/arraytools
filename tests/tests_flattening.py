import unittest

from mock import MagicMock, patch

from arraytools.flattening import (
    flatten,
    flatten_integers
)


class TestFlattenMethod(unittest.TestCase):

    def setUp(self):
        self.mocked_object = MagicMock()

    def test_no_recursion(self):
        self.assertEqual(
            flatten([1, 'a', self.mocked_object]),
            [1, 'a', self.mocked_object]
        )

    def test_recursion(self):
        self.assertEqual(
            flatten([1, [2, [3, ['a', [self.mocked_object]]]]]),
            [1, 2, 3, 'a', self.mocked_object]
        )

    def test_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_non_array_input_error(self):
        with self.assertRaises(TypeError) as non_array:
            flatten('hello world')
        self.assertEqual(
            str(non_array.exception),
            "Input must be in (<type 'list'>, <type 'tuple'>, <type 'set'>)"
        )

    def test_array_input_not_allowed_element_error(self):
        with self.assertRaises(TypeError) as not_allowed:
            flatten(['hello world'], (int))
        self.assertEqual(
            str(not_allowed.exception),
            ("Array must contain (<type 'list'>, <type 'tuple'>, <type 'set'>)"
             " or <type 'int'>")
        )


class TestFlattenIntegersMethod(unittest.TestCase):

    @patch('arraytools.flattening.flatten')
    def test_flatten_integers(self, p_flatten):
        flatten_integers([1, 2, 3, [4]])
        p_flatten.assert_called_once_with([1, 2, 3, [4]], (int))
