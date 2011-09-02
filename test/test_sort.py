import test_base
import unittest
from datetime import *

from gpipes.models import Entry
from gpipes.filter import sort


class SortFilterTest(test_base.GAETestBase):
    def test_execute_default(self):
        environ = {}
        config = {}
        plugin = sort.SortFilter(config, environ)

        content = {
                "entries": [
                    {
                        "title": "bar",
                        "link": "http://example.com/bar",
                        "updated_parsed": (2010, 2, 2, 12, 0, 0),
                        },
                    {
                        "title": "foo",
                        "link": "http://example.com/foo",
                        "updated_parsed": (2010, 2, 1, 12, 0, 0),
                        },
                    ],
                }
        content = plugin.execute(content)
        self.assertEqual("foo", content["entries"][0]["title"])
        self.assertEqual("bar", content["entries"][1]["title"])

    def test_execute_key(self):
        environ = {}
        config = {
            "key": "title",
            }
        plugin = sort.SortFilter(config, environ)

        content = {
                "entries": [
                    {
                        "title": "foo",
                        "link": "http://example.com/foo",
                        "updated_parsed": (2010, 2, 1, 12, 0, 0),
                        },
                    {
                        "title": "bar",
                        "link": "http://example.com/bar",
                        "updated_parsed": (2010, 2, 2, 12, 0, 0),
                        },
                    ],
                }
        content = plugin.execute(content)
        self.assertEqual("bar", content["entries"][0]["title"])
        self.assertEqual("foo", content["entries"][1]["title"])

    def test_execute_reverse(self):
        environ = {}
        config = {
            "reverse": True
            }
        plugin = sort.SortFilter(config, environ)

        content = {
                "entries": [
                    {
                        "title": "foo",
                        "link": "http://example.com/foo",
                        "updated_parsed": (2010, 2, 1, 12, 0, 0),
                        },
                    {
                        "title": "bar",
                        "link": "http://example.com/bar",
                        "updated_parsed": (2010, 2, 2, 12, 0, 0),
                        },
                    ],
                }
        content = plugin.execute(content)
        self.assertEqual("bar", content["entries"][0]["title"])
        self.assertEqual("foo", content["entries"][1]["title"])


if __name__ == '__main__':
    unittest.main()

