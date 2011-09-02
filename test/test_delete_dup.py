import test_base
import unittest
from datetime import *

from gpipes.models import Entry
from gpipes.filter import delete_dup 


class DeleteDuplicatedLinkFilterTest(test_base.GAETestBase):
    def test_execute(self):
        environ = {}
        config = {}
        plugin = delete_dup.DeleteDuplicatedLinkFilter(config, environ)

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
                    {
                        "title": "bar",
                        "link": "http://example.com/bar",
                        "updated_parsed": (2010, 2, 3, 12, 0, 0),
                        },
                    ],
                }
        content = plugin.execute(content)

        self.assertEqual(2, len(content["entries"]))


if __name__ == '__main__':
    unittest.main()

