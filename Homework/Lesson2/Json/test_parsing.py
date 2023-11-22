import json
import unittest
from unittest.mock import *
from parsing_json import *


class TestParser(unittest.TestCase):

    def test_parse(self):
        file_name = "test.json"
        with open(file_name) as f:
            file_content = f.read()
            json_content = json.loads(file_content)

        required_fields = {"key1"}
        keywords = {"word1", "Word2"}
        function = MagicMock()
        parsing(json_content, function, required_fields, keywords)

        self.assertEqual(2, function.call_count)
        function.assert_any_call("word1")
        function.assert_any_call("Word2")


if __name__ == '__main__':
    unittest.main()
