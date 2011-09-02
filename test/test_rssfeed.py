import test_base
import unittest
from datetime import datetime
from gpipes.models import Feed
from gpipes.publisher import rssfeed


class RssFeedPublisherTest(test_base.GAETestBase):
    def test_execute(self):
        config = {
            "title": "test",
            "link": "http://example.com/rss",
            "description": "test",
        }
        environ = {
            "pipeline_name": "test",
                }
        plugin = rssfeed.create(config, environ)

        content = {
            "entries": [{
                "title": "test",
                "link": "http://d.hatena.ne.jp/griefworker/",
                "summary": "test",
                "updated_parsed": datetime.now().timetuple(),
            }],
        }
        content = plugin.execute(content)

        self.assertEqual(1, len(content["entries"]))
        self.assertEqual(1, Feed.all().count())


if __name__ == '__main__':
    unittest.main()

