import test_base
import unittest
from datetime import *

from gpipes.models import Entry
from gpipes.filter import readmore


class ReadMoreFilterTest(test_base.GAETestBase):
    def test_execute(self):
        config = {}
        environ = {}
        plugin = readmore.create(config, environ)

        content = {
                "entries": [
                    {
                        "link": "http://example.com/foo",
                        "summary": "test",
                        },
                    {
                        "link": "http://example.com/bar",
                        "summary": "test",
                        },
                    ],
                }
        content = plugin.execute(content)

        # Debug
        for entry in content["entries"]:
            print(entry["summary"])

        self.assertNotEqual("test", content["entries"][0]["summary"])
        self.assertNotEqual("test", content["entries"][1]["summary"])


if __name__ == '__main__':
    unittest.main()

