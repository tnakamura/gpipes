# -*- coding : utf-8 -*-


from datetime import *


class Mock(object):
    def __init__(self, config, environ):
        pass

    def execute(self, content):
        content["feed"] = {
            "id": "http://test.com/",
            "title": "test",
            "link": "http://test.com/",
        }
        content["entries"] = [
            {
                "title": "foo",
                "link": "http://test.com/foo",
                "summary": "foo",
                "updated_parsed": datetime.now().timetuple(),
                "author": "foo",
            },
            {
                "title": "bar",
                "link": "http://test.com/bar",
                "summary": "bar",
                "updated_parsed": datetime.now().timetuple(),
                "author": "bar",
            },
        ]
        return content


def create(config, environ):
    return Mock(config, environ)

