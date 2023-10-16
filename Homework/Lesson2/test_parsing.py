import json
import sys
import unittest
from unittest.mock import *
from parsing_json import *


class TestParser(unittest.TestCase):

    def test_parse(self):
        if len(sys.argv) != 2:
            return 1

        file_name = sys.argv[1]
        with open(file_name) as f:
            file_content = f.read()
            json_content = json.loads(file_content)

        required_fields = {"key1"}
        keywords = {"word1"}
        function = MagicMock(name="func")

        # Запуск без mock-объекта
        # required_fields = read_fields()
        # keywords = read_values()
        # parsing(json_content, func, required_fields, keywords)

        parsing(json_content, function, required_fields, keywords)

        expected = [call("word1")]

        self.assertEqual(expected[0], function.mock_calls[0])
        self.assertEqual(1, function.call_count)


if __name__ == '__main__':
    unittest.main()
