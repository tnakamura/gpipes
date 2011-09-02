import test_base
import unittest


from datetime import datetime
from gpipes.publisher import mail


class MailPublisherTest(test_base.GAETestBase):
    def test_execute(self):
        config = {
                "sender_address":"test@example.com",
                "user_address": "griefworker@gmail.com",
                "subject": "mail test",
                }
        environ = {}
        plugin = mail.create(config, environ)

        content = {
                "entries": [{
                    "title": "foo",
                    "link": "http://d.hatena.ne.jp/griefworker/20100406/foo",
                    "summary": "foo summary",
                    "updated_parsed": datetime.now().timetuple(),
                    },
                    {
                        "title": "bar",
                        "link": "http://d.hatena.ne.jp/griefworker/20100406/bar",
                        "summary": "bar summary",
                        "updated_parsed": datetime.now().timetuple(),
                        }],
                    }
        content = plugin.execute(content)


if __name__ == '__main__':
    unittest.main()

