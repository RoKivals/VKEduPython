import unittest
from lru_cache import LRUCache


class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

    def test_get(self):
        self.assertIsNone(self.cache.get("k3"))
        self.assertEqual(self.cache.get("k2"), "val2")
        self.assertEqual(self.cache.get("k1"), "val1")

    def test_overflow_cache(self):
        pass
        # self.cache.set("k3", "val3")
        # assert cache.get("k3")) == "val3"
        # assert cache.get("k2")) is None
        # assert cache.get("k1")) == "val1"
