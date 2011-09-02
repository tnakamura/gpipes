import test_base
import unittest


from gpipes.filter import grep


class ReadMoreFilterTest(test_base.GAETestBase):
    def test_execute(self):
        config = {
                "key": "link",
                "pattern": "http://d.hatena.ne.jp/griefworker/[0-9]+/[0-9]+",
                }
        environ = {}
        plugin = grep.create(config, environ)

        content = {
                "entries": [
                    {
                        "link": "http://d.hatena.ne.jp/griefworker/20100405/12345678",
                        "summary": "FooBar",
                        },
                    {
                        "link": "http://d.hatena.ne.jp/griefworker/20100405/hoge_fuga",
                        "summary": "HogeFuga",
                        },
                    ],
                }
        content = plugin.execute(content)

        self.assertEqual(1, len(content["entries"]))
        self.assertEqual("FooBar", content["entries"][0]["summary"])

    def test_execute_exclusive(self):
        config = {
                "key": "link",
                "pattern": "http://d.hatena.ne.jp/griefworker/[0-9]+/[0-9]+",
                "exclusive": True,
                }
        environ = {}
        plugin = grep.create(config, environ)

        content = {
                "entries": [
                    {
                        "link": "http://d.hatena.ne.jp/griefworker/20100405/12345678",
                        "summary": "FooBar",
                        },
                    {
                        "link": "http://d.hatena.ne.jp/griefworker/20100405/hoge_fuga",
                        "summary": "HogeFuga",
                        },
                    ],
                }
        content = plugin.execute(content)

        self.assertEqual(1, len(content["entries"]))
        self.assertEqual("HogeFuga", content["entries"][0]["summary"])


if __name__ == '__main__':
    unittest.main()

