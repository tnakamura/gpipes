import test_base
import unittest


from datetime import datetime
from gpipes.models import Entry
from gpipes.publisher import xmlrpc


class XmlRpcPublisherTest(test_base.GAETestBase):
    def test_execute(self):
        config = {
            "username":"username",
            "password":"password",
            "api_url":"api_url",
        }
        environ = {}
        plugin = xmlrpc.create(config, environ)

        content = {
            "entries": [{
                "title": "test",
                "link": "http://d.hatena.ne.jp/griefworker/",
                "summary": "test",
                "updated_parsed": datetime.now().timetuple(),
            }],
        }
        content = plugin.execute(content)


if __name__ == '__main__':
    unittest.main()

