import test_base
import unittest
from datetime import *

from gpipes import models
from gpipes.filter import unread

RED_URL = "http://example.com/foo"

class UnreadFilterTest(test_base.GAETestBase):
    def test_execute(self):
        feed_key_name = models.Feed.create_key_name("test")
        feed = models.Feed.get_or_insert(feed_key_name)

        key_name = models.Entry.create_key_name("test", RED_URL)
        entry = models.Entry(key_name=key_name, parent=feed)
        entry.title = "foo"
        entry.summary = "foo"
        entry.url = RED_URL 
        entry.updated = datetime(2010, 2, 1, 12, 0, 0)
        entry.put()

        config = {}
        environ = {
                "pipeline_name": "test",
                }
        plugin = unread.create(config, environ)
        content = {
                "entries": [
                    {
                        "link": RED_URL,
                        "updated_parsed": (2010, 2, 1, 12, 0, 0),
                        },
                    {
                        "link": "http://example.com/bar",
                        "updated_parsed": (2010, 2, 2, 12, 0, 0),
                        },
                    ],
                }

        content = plugin.execute(content)
        self.assertEqual(1, len(content["entries"]))


if __name__ == '__main__':
    unittest.main()

