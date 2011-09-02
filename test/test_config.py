import test_base
import unittest
from gpipes.subscription import config


class ConfigTest(test_base.GAETestBase):
    def test_execute(self):
        plugin_config = {
                "feed": [
                    "http://d.hatena.ne.jp/griefworker/rss",
                    ],
                }
        environ = {}

        plugin = config.create(plugin_config, environ)
        content = plugin.execute({ "entries": [] })
        self.assert_(0 < len(content["entries"]))

        for entry in content["entries"]:
            print(entry["title"])
            print(entry["link"])
            print("\n")


if __name__ == '__main__':
    unittest.main()

