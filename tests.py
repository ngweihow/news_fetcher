import unittest
from unittest.mock import Mock

from parser_interface import Parser
from parser_factory import ParserFactory
from ninenews_parser import NineNewsParser


class MyTestCase(unittest.TestCase):

    def test_parser_factory_create_parser_pass(self):
        """
        Test Factor creates right parser.
        """
        parser: Parser = ParserFactory.create_parser("https://www.9news.com.au/just-in")
        self.assertTrue(isinstance(parser, NineNewsParser))

    def test_parser_factory_create_parser_fail(self):
        """
        Test Factor creates wrong parser.
        """
        parser: Parser = ParserFactory.create_parser("abc")
        self.assertFalse(isinstance(parser, NineNewsParser))


if __name__ == '__main__':
    unittest.main()
