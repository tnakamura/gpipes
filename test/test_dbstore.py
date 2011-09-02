import test_base
import unittest
from datetime import datetime

from gpipes.models import Entry
from gpipes.publisher import dbstore


class DatastorePublisherTest(test_base.GAETestBase):
    def test_execute(self):
        config = {}
        environ = {
            "pipeline_name": "test",
            }
        plugin = dbstore.create(config, environ)

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

        entries = Entry.all()
        self.assertEqual(1, entries.count())


if __name__ == '__main__':
    unittest.main()

